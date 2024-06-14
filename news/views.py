from django.shortcuts import render



import requests
from django.shortcuts import render
from django.conf import settings

def index(request):
    api_key = settings.NEWS_API_KEY
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get('articles', [])

    return render(request, 'news\index.html', {'articles': articles})

