"""
Wellness Tips Module

This module fetches wellness tips related to plant-based nutrition.
It provides tips for self-care, nutrition, and healthy living.
"""

import os
import requests
import random
from bs4 import BeautifulSoup
from config import current_config

def scrape_wellness_tips():
    """
    Scrape wellness tips from reputable websites.
    
    Returns:
        list: A list of wellness tips.
    """
    try:
        # List of URLs to scrape
        urls = [
            'https://www.health.harvard.edu/blog/what-is-a-plant-based-diet-and-why-should-you-try-it-2018092614760',
            'https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/vegetarian-diet/art-20046446',
            'https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/nutrition-basics/how-does-plant-forward-eating-benefit-your-health'
        ]
        
        # Randomly select one URL to scrape
        url = random.choice(urls)
        
        # Send request to the website
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            raise Exception(f"Failed to fetch content from {url}")
            
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find paragraphs that might contain wellness tips
        paragraphs = soup.find_all('p')
        
        # Extract potential tips (paragraphs with reasonable length)
        potential_tips = []
        for p in paragraphs:
            text = p.get_text().strip()
            if 50 < len(text) < 200 and not text.startswith('Copyright') and not text.startswith('©'):
                potential_tips.append({
                    'content': text,
                    'source': url,
                    'source_name': url.split('/')[2].replace('www.', '')
                })
                
        # Return a random selection of tips
        if potential_tips:
            return random.sample(potential_tips, min(5, len(potential_tips)))
        else:
            return []
            
    except Exception as e:
        print(f"Error scraping wellness tips: {str(e)}")
        return []

def get_fallback_tips():
    """
    Provide fallback wellness tips when scraping fails.
    
    Returns:
        list: A list of fallback wellness tips.
    """
    return [
        {
            'content': 'Aim for at least 5 servings of fruits and vegetables each day to ensure you get a variety of nutrients.',
            'source': 'https://example.com/nutrition-tips',
            'source_name': 'example.com'
        },
        {
            'content': 'Stay hydrated by drinking water throughout the day. Try infusing water with fruits or herbs for added flavor.',
            'source': 'https://example.com/hydration-tips',
            'source_name': 'example.com'
        },
        {
            'content': 'Include a variety of plant proteins such as beans, lentils, tofu, and tempeh in your diet for essential amino acids.',
            'source': 'https://example.com/protein-tips',
            'source_name': 'example.com'
        },
        {
            'content': 'Practice mindful eating by savoring each bite and paying attention to hunger and fullness cues.',
            'source': 'https://example.com/mindful-eating',
            'source_name': 'example.com'
        },
        {
            'content': 'Take time for self-care activities such as meditation, yoga, or simply spending time in nature.',
            'source': 'https://example.com/self-care',
            'source_name': 'example.com'
        }
    ]

def fetch_wellness_tips():
    """
    Fetch wellness tips related to plant-based nutrition.
    
    This function combines scraped tips with fallback tips
    to ensure there are always tips available.
    
    Returns:
        list: A list of wellness tips.
    """
    try:
        # Try to scrape wellness tips
        scraped_tips = scrape_wellness_tips()
        
        # If scraping fails or returns no tips, use fallback tips
        if not scraped_tips:
            tips = get_fallback_tips()
        else:
            tips = scraped_tips
            
        # Limit to the maximum number of tips
        return tips[:current_config.MAX_WELLNESS_TIPS]
    except Exception as e:
        print(f"Error in fetch_wellness_tips: {str(e)}")
        return get_fallback_tips()[:current_config.MAX_WELLNESS_TIPS]
