"""
Email Sender Module

This module handles sending the newsletter to recipients via email.
It uses Flask-Mail to send HTML emails.
"""

import os
from flask import current_app
from flask_mail import Mail, Message
from datetime import datetime
from config import current_config

def send_newsletter(recipients, html_content):
    """
    Send the newsletter to the specified recipients.
    
    Args:
        recipients (list): A list of email addresses to send the newsletter to.
        html_content (str): The HTML content of the newsletter.
        
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    try:
        # Initialize Flask-Mail
        mail = Mail(current_app)
        
        # Create the message
        subject = f"{current_config.NEWSLETTER_TITLE} - {datetime.now().strftime('%B %d, %Y')}"
        msg = Message(
            subject=subject,
            recipients=recipients,
            html=html_content,
            sender=current_config.MAIL_DEFAULT_SENDER
        )
        
        # Send the message
        mail.send(msg)
        
        # Log the successful send
        current_app.logger.info(f"Newsletter sent to {len(recipients)} recipients")
        
        return {
            'success': True,
            'message': f"Newsletter sent to {len(recipients)} recipients"
        }
    except Exception as e:
        # Log the error
        current_app.logger.error(f"Error sending newsletter: {str(e)}")
        
        return {
            'success': False,
            'error': str(e)
        }

def send_test_email(recipient):
    """
    Send a test email to verify email configuration.
    
    Args:
        recipient (str): The email address to send the test email to.
        
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    try:
        # Initialize Flask-Mail
        mail = Mail(current_app)
        
        # Create the message
        subject = f"Test Email from {current_config.COMPANY_NAME}"
        body = f"""
        <html>
        <body>
            <h1>Test Email</h1>
            <p>This is a test email from the {current_config.NEWSLETTER_TITLE} system.</p>
            <p>If you received this email, your email configuration is working correctly.</p>
            <p>Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </body>
        </html>
        """
        
        msg = Message(
            subject=subject,
            recipients=[recipient],
            html=body,
            sender=current_config.MAIL_DEFAULT_SENDER
        )
        
        # Send the message
        mail.send(msg)
        
        # Log the successful send
        current_app.logger.info(f"Test email sent to {recipient}")
        
        return {
            'success': True,
            'message': f"Test email sent to {recipient}"
        }
    except Exception as e:
        # Log the error
        current_app.logger.error(f"Error sending test email: {str(e)}")
        
        return {
            'success': False,
            'error': str(e)
        }
