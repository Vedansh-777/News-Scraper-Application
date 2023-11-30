# newsapp/views.py
from django.shortcuts import render
from .news_scraper import get_news

def news_view(request):
    news_articles = []
    person_name = ''

    if request.method == 'POST':
        person_name = request.POST.get('person_name', '')
        news_articles = get_news(person_name)

    return render(request, 'news/index.html', {'news_articles': news_articles, 'person_name': person_name})


