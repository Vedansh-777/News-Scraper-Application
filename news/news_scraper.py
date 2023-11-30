import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

def extract_summary(article):
    # Try to find summary directly within the article
    summary_element = article.find('div')
    summary = summary_element.get_text(strip=True) if summary_element else "No Summary"
    
    # Break summary at the word 'More' and extract only the part before it
    summary_parts = re.split(r'\bMore\b', summary, flags=re.IGNORECASE)
    site_name = summary_parts[0].strip()
    print(site_name)

    return site_name

def get_news(person_name):
    # Function to fetch and display news related to a person from Google News

    # Google News URL
    url = f'https://news.google.com/search?q={person_name}&hl=en-US&gl=US&ceid=US%3Aen'

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find news articles
            articles = soup.find_all('article')

            # Get today's date
            today = datetime.now().date()

            # Create a list to store articles with their details
            news_articles = []

            # Extract and store details of news articles
            for article in articles:
                # Extract article title (trying different tags)
                title_element = article.find(['h3', 'h4', 'h5', 'h6'])
                title = title_element.get_text(strip=True) if title_element else "No Title"

                # Extract article summary
                summary_element = article.find('div',{'class':'vr1PYe'})
                summary = summary_element.get_text() if title_element else "No Title"


                # Extract article date
                date_str = article.find('time')['datetime']
                article_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').date()

                # Calculate the number of days ago the article was published
                days_ago = (today - article_date).days

                # Check if the article is within the last 5 days
                if days_ago <= 5:
                    # Append article details to the list
                    news_articles.append({
                        'title': title,
                        'summary': summary,
                        'days_ago': days_ago
                    })

            # Sort articles by publication date (latest first)
            news_articles = sorted(news_articles, key=lambda x: x['days_ago'])

            # Display the latest news articles from the last 5 days
            for article in news_articles:
                print(f"Title: {article['title']}")
                print(f"Summary: {article['summary']}")
                print(f"Published {article['days_ago']} days ago\n")

            # Return the list of news articles
            return news_articles

        else:
            print(f"Error: Unable to fetch news. Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")