"""
Weekly Wellness Newsletter Generator - Main Application

This Flask application serves as the main entry point for the Weekly Wellness Newsletter Generator.
It provides routes for the admin dashboard, newsletter preview, and sending functionality.
"""

import os
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from modules.news_fetcher import fetch_trending_news
from modules.recipe_fetcher import fetch_recipes
from modules.wellness_tips import fetch_wellness_tips
from modules.email_sender import send_newsletter

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev_key_for_demo')

# Context processor to add variables to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}

@app.route('/')
def index():
    """Render the home page."""
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"Error rendering index page: {str(e)}")
        return render_template('error.html', error=str(e))

@app.route('/admin')
def admin_dashboard():
    """Render the admin dashboard."""
    try:
        return render_template('dashboard.html')
    except Exception as e:
        app.logger.error(f"Error rendering admin dashboard: {str(e)}")
        return render_template('error.html', error=str(e))

@app.route('/preview')
def preview_newsletter():
    """
    Generate and preview the newsletter with the latest content.
    
    This route fetches the latest trending news, recipes, and wellness tips
    and renders them in the newsletter template for preview.
    """
    try:
        # Fetch content for the newsletter
        news = fetch_trending_news()
        recipes = fetch_recipes()
        tips = fetch_wellness_tips()
        
        # Render the newsletter template with the fetched content
        return render_template(
            'newsletter.html',
            news=news,
            recipes=recipes,
            tips=tips,
            preview=True
        )
    except Exception as e:
        app.logger.error(f"Error previewing newsletter: {str(e)}")
        return render_template('error.html', error=str(e))

@app.route('/send', methods=['POST'])
def send_newsletter_route():
    """
    Send the newsletter to the specified email addresses.
    
    This route handles the form submission from the admin dashboard
    and sends the newsletter to the provided email addresses.
    """
    try:
        if request.method == 'POST':
            recipients = request.form.get('recipients', '').split(',')
            recipients = [email.strip() for email in recipients if email.strip()]
            
            if not recipients:
                flash('Please provide at least one recipient email address.', 'error')
                return redirect(url_for('admin_dashboard'))
            
            # Fetch content for the newsletter
            news = fetch_trending_news()
            recipes = fetch_recipes()
            tips = fetch_wellness_tips()
            
            # Generate the newsletter HTML
            newsletter_html = render_template(
                'newsletter.html',
                news=news,
                recipes=recipes,
                tips=tips,
                preview=False
            )
            
            # Send the newsletter
            send_result = send_newsletter(recipients, newsletter_html)
            
            if send_result['success']:
                flash(f'Newsletter sent successfully to {len(recipients)} recipients!', 'success')
            else:
                flash(f'Error sending newsletter: {send_result["error"]}', 'error')
                
            return redirect(url_for('admin_dashboard'))
    except Exception as e:
        app.logger.error(f"Error sending newsletter: {str(e)}")
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('admin_dashboard'))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('error.html', error='Page not found'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return render_template('error.html', error='Server error'), 500

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Run the Flask application
    app.run(debug=True)
