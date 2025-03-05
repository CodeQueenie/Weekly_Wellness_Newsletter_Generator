"""
News Fetcher Module

This module fetches trending plant-based nutrition news from various sources.
It uses the Google Trends API and News API to find relevant articles.
"""

import os
import requests
from datetime import datetime, timedelta
from pytrends.request import TrendReq
from newsapi import NewsApiClient
from config import current_config

def fetch_trending_topics():
    """
    Fetch trending topics related to plant-based nutrition from Google Trends.
    
    Returns:
        list: A list of trending topics.
    """
    try:
        # Initialize pytrends
        pytrends = TrendReq(hl='en-US', tz=360)
        
        # Build payload
        keywords = ['plant based', 'vegan', 'vegetarian', 'nutrition', 'wellness']
        pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='US', gprop='')
        
        # Get related queries
        related_queries = pytrends.related_queries()
        
        # Extract trending topics
        trending_topics = []
        for keyword in keywords:
            if related_queries[keyword] and 'top' in related_queries[keyword]:
                top_queries = related_queries[keyword]['top']
                if not top_queries.empty:
                    for _, row in top_queries.head(3).iterrows():
                        trending_topics.append(row['query'])
        
        return trending_topics[:5]  # Return top 5 trending topics
    except Exception as e:
        print(f"Error fetching trending topics: {str(e)}")
        return ['plant based diet', 'vegan recipes', 'vegetarian protein', 'nutrition tips', 'wellness routine']

def fetch_news_articles(topics):
    """
    Fetch news articles related to the given topics using News API.
    
    Args:
        topics (list): A list of topics to search for.
        
    Returns:
        list: A list of news articles.
    """
    try:
        # Initialize News API client
        newsapi = NewsApiClient(api_key=current_config.NEWS_API_KEY)
        
        # Calculate date range (last 7 days)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        # Format dates for News API
        from_date = start_date.strftime('%Y-%m-%d')
        to_date = end_date.strftime('%Y-%m-%d')
        
        # Fetch articles for each topic
        all_articles = []
        for topic in topics:
            response = newsapi.get_everything(
                q=topic,
                from_param=from_date,
                to=to_date,
                language='en',
                sort_by='relevancy',
                page=1,
                page_size=3
            )
            
            if response['status'] == 'ok' and response['totalResults'] > 0:
                for article in response['articles']:
                    all_articles.append({
                        'title': article['title'],
                        'description': article['description'],
                        'url': article['url'],
                        'source': article['source']['name'],
                        'published_at': article['publishedAt'],
                        'image_url': article['urlToImage']
                    })
        
        # Remove duplicates based on URL
        unique_articles = []
        seen_urls = set()
        for article in all_articles:
            if article['url'] not in seen_urls:
                seen_urls.add(article['url'])
                unique_articles.append(article)
        
        return unique_articles[:current_config.MAX_NEWS_ITEMS]
    except Exception as e:
        print(f"Error fetching news articles: {str(e)}")
        # Return fallback articles if API fails
        return [
            {
                'title': 'The Benefits of a Plant-Based Diet',
                'description': 'Discover how a plant-based diet can improve your health and well-being.',
                'url': 'https://example.com/plant-based-diet',
                'source': 'Wellness Magazine',
                'published_at': datetime.now().isoformat(),
                'image_url': '/static/images/plant-based-diet.jpg'
            },
            {
                'title': 'Top 10 Plant-Based Protein Sources',
                'description': 'Learn about the best plant-based sources of protein for a balanced diet.',
                'url': 'https://example.com/plant-based-protein',
                'source': 'Nutrition Today',
                'published_at': datetime.now().isoformat(),
                'image_url': '/static/images/plant-protein.jpg'
            },
            {
                'title': 'How to Transition to a Plant-Based Lifestyle',
                'description': 'Tips and tricks for transitioning to a plant-based lifestyle.',
                'url': 'https://example.com/plant-based-lifestyle',
                'source': 'Health & Wellness',
                'published_at': datetime.now().isoformat(),
                'image_url': '/static/images/plant-lifestyle.jpg'
            }
        ]

def fetch_trending_news():
    """
    Fetch trending plant-based nutrition news.
    
    This function combines the trending topics and news articles
    to provide a curated list of trending news.
    
    Returns:
        list: A list of trending news articles.
    """
    try:
        # Fetch trending topics
        topics = fetch_trending_topics()
        
        # Fetch news articles for those topics
        articles = fetch_news_articles(topics)
        
        return articles
    except Exception as e:
        print(f"Error in fetch_trending_news: {str(e)}")
        # Return fallback articles if something goes wrong
        return [
            {
                'title': 'The Benefits of a Plant-Based Diet',
                'description': 'Discover how a plant-based diet can improve your health and well-being.',
                'url': 'https://example.com/plant-based-diet',
                'source': 'Wellness Magazine',
                'published_at': datetime.now().isoformat(),
                'image_url': '/static/images/plant-based-diet.jpg'
            },
            {
                'title': 'Top 10 Plant-Based Protein Sources',
                'description': 'Learn about the best plant-based sources of protein for a balanced diet.',
                'url': 'https://example.com/plant-based-protein',
                'source': 'Nutrition Today',
                'published_at': datetime.now().isoformat(),
                'image_url': '/static/images/plant-protein.jpg'
            },
            {
                'title': 'How to Transition to a Plant-Based Lifestyle',
                'description': 'Tips and tricks for transitioning to a plant-based lifestyle.',
                'url': 'https://example.com/plant-based-lifestyle',
                'source': 'Health & Wellness',
                'published_at': datetime.now().isoformat(),
                'image_url': '/static/images/plant-lifestyle.jpg'
            }
        ]
