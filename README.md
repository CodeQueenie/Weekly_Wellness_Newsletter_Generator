# Weekly Wellness Newsletter Generator

A Flask-based application that generates weekly wellness newsletters for a plant-based nutrition company. This application fetches trending plant-based nutrition news, self-care tips, and recipes, and formats them into an email newsletter.

## Open-Source Components (This Repository)

This repository contains the open-source demo version of the Weekly Wellness Newsletter Generator with the following features:

- Flask web application with an admin dashboard
- Integration with public APIs to fetch trending wellness news
- Recipe curation from public sources
- Responsive email template for newsletters
- Error handling and fallback content

## Private Components (Not Included)

The following features are part of the private, proprietary implementation and are not included in this repository:

- AI-generated wellness tips & personalized recommendations
- Auto-scheduling for weekly email delivery
- Advanced SEO optimization for content ranking
- User database for email preferences & analytics
- Custom analytics dashboard for tracking engagement

## Setup and Installation

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/weekly-wellness-newsletter.git
   cd weekly-wellness-newsletter
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   
4. Create a `.env` file in the root directory based on the `.env.example` file:
   ```
   # Flask configuration
   SECRET_KEY=your_secret_key
   FLASK_ENV=development
   FLASK_APP=app.py

   # API Keys
   GOOGLE_TRENDS_API_KEY=your_google_trends_api_key
   NEWS_API_KEY=your_news_api_key
   RECIPE_API_KEY=your_recipe_api_key

   # Email configuration
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_app_password
   MAIL_DEFAULT_SENDER=your_email@gmail.com
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
weekly-wellness-newsletter/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Required packages
├── .env.example            # Example environment variables
├── .env                    # Environment variables (not tracked by git)
├── .gitignore              # Git ignore file
├── static/                 # Static files (CSS, JS, images)
│   ├── css/                # CSS files
│   ├── js/                 # JavaScript files
│   └── images/             # Image files
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── index.html          # Home page
│   ├── dashboard.html      # Admin dashboard
│   ├── newsletter.html     # Newsletter template
│   └── error.html          # Error page
└── modules/                # Application modules
    ├── news_fetcher.py     # Module to fetch trending news
    ├── recipe_fetcher.py   # Module to fetch recipes
    ├── wellness_tips.py    # Module to fetch wellness tips
    └── email_sender.py     # Module to send emails
```

## Usage

1. Access the home page at `http://127.0.0.1:5000/`
2. View the admin dashboard at `http://127.0.0.1:5000/admin`
3. Preview the newsletter at `http://127.0.0.1:5000/preview`
4. Send the newsletter to test email addresses from the preview page

## Features

- **Admin Dashboard**: Manage and monitor newsletter content and sending status
- **Content Curation**: Automatically fetch trending plant-based nutrition news
- **Recipe Integration**: Include plant-based recipes in each newsletter
- **Wellness Tips**: Provide helpful wellness tips related to plant-based nutrition
- **Responsive Design**: Newsletter displays properly on all devices
- **Fallback Content**: Default content available when API keys are not configured

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
