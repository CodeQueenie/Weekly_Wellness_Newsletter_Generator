"""
Configuration settings for the Weekly Wellness Newsletter Generator.

This module contains configuration settings for the application,
including API keys and other environment-specific variables.

Copyright (c) 2025 Nicole LeGuern
Licensed under MIT License with attribution requirements
https://github.com/CodeQueenie/Weekly_Wellness_Newsletter_Generator
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration class."""
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key_for_demo')
    DEBUG = False
    TESTING = False
    
    # API keys
    GOOGLE_TRENDS_API_KEY = os.getenv('GOOGLE_TRENDS_API_KEY')
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    RECIPE_API_KEY = os.getenv('RECIPE_API_KEY')
    
    # Email configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() in ('true', '1', 't')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    
    # Newsletter configuration
    NEWSLETTER_TITLE = os.getenv('NEWSLETTER_TITLE', 'Weekly Wellness Newsletter')
    COMPANY_NAME = os.getenv('COMPANY_NAME', 'Plant-Based Nutrition Co.')
    COMPANY_LOGO_URL = os.getenv('COMPANY_LOGO_URL', '/static/images/logo.png')
    COMPANY_WEBSITE = os.getenv('COMPANY_WEBSITE', 'https://example.com')
    
    # Content configuration
    MAX_NEWS_ITEMS = int(os.getenv('MAX_NEWS_ITEMS', 3))
    MAX_RECIPES = int(os.getenv('MAX_RECIPES', 2))
    MAX_WELLNESS_TIPS = int(os.getenv('MAX_WELLNESS_TIPS', 3))

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    # Production-specific settings
    pass

# Dictionary of configuration environments
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Get the current configuration
current_config = config[os.getenv('FLASK_ENV', 'default')]
