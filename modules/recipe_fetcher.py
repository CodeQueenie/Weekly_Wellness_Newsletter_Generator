"""
Recipe Fetcher Module

This module fetches plant-based recipes from various sources.
It uses public recipe APIs to find relevant recipes.
"""

import os
import requests
import random
from datetime import datetime
from config import current_config

def fetch_recipes_from_api():
    """
    Fetch plant-based recipes from a recipe API.
    
    Returns:
        list: A list of recipes.
    """
    try:
        # API endpoint
        api_key = current_config.RECIPE_API_KEY
        if not api_key:
            raise ValueError("Recipe API key not found")
            
        # Example using Spoonacular API
        url = f"https://api.spoonacular.com/recipes/complexSearch"
        params = {
            'apiKey': api_key,
            'diet': 'vegan',
            'number': 5,
            'addRecipeInformation': 'true',
            'fillIngredients': 'true',
            'sort': 'random'
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}: {data.get('message', '')}")
        
        recipes = []
        for item in data.get('results', []):
            recipe = {
                'title': item.get('title', ''),
                'image_url': item.get('image', ''),
                'source_url': item.get('sourceUrl', ''),
                'ready_in_minutes': item.get('readyInMinutes', 0),
                'servings': item.get('servings', 0),
                'summary': item.get('summary', ''),
                'ingredients': [ingredient.get('original', '') for ingredient in item.get('extendedIngredients', [])]
            }
            recipes.append(recipe)
            
        return recipes
    except Exception as e:
        print(f"Error fetching recipes from API: {str(e)}")
        return []

def get_fallback_recipes():
    """
    Provide fallback recipes when the API is unavailable.
    
    Returns:
        list: A list of fallback recipes.
    """
    return [
        {
            'title': 'Vegan Buddha Bowl',
            'image_url': '/static/images/buddha-bowl.jpg',
            'source_url': 'https://example.com/vegan-buddha-bowl',
            'ready_in_minutes': 30,
            'servings': 2,
            'summary': 'A nutritious and colorful Buddha bowl packed with plant-based goodness.',
            'ingredients': [
                '1 cup quinoa, cooked',
                '1 cup chickpeas, roasted',
                '1 avocado, sliced',
                '1 cup kale, massaged',
                '1 cup sweet potato, roasted',
                '2 tbsp tahini dressing'
            ]
        },
        {
            'title': 'Plant-Based Lentil Soup',
            'image_url': '/static/images/lentil-soup.jpg',
            'source_url': 'https://example.com/lentil-soup',
            'ready_in_minutes': 45,
            'servings': 4,
            'summary': 'A hearty and warming lentil soup that\'s perfect for cold days.',
            'ingredients': [
                '2 cups red lentils',
                '1 onion, diced',
                '2 carrots, diced',
                '2 celery stalks, diced',
                '4 cups vegetable broth',
                '1 tsp cumin',
                '1 tsp turmeric',
                'Salt and pepper to taste'
            ]
        }
    ]

def fetch_recipes():
    """
    Fetch plant-based recipes.
    
    This function combines API results with fallback recipes
    to ensure there are always recipes available.
    
    Returns:
        list: A list of recipes.
    """
    try:
        # Try to fetch recipes from API
        api_recipes = fetch_recipes_from_api()
        
        # If API fails or returns no recipes, use fallback recipes
        if not api_recipes:
            recipes = get_fallback_recipes()
        else:
            recipes = api_recipes
            
        # Limit to the maximum number of recipes
        return recipes[:current_config.MAX_RECIPES]
    except Exception as e:
        print(f"Error in fetch_recipes: {str(e)}")
        return get_fallback_recipes()[:current_config.MAX_RECIPES]
