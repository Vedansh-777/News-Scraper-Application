import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

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
            articles = soup.find_all('div', {'class': 'xrnccd'})

            # Get today's date
            today = datetime.now().date()

            # Display news headlines and summaries from the last 5 days
            for article in articles:
                # Extract article title
                title_element = article.find('h3', {'class': 'ipQwMb'})
                title = title_element.get_text() if title_element else "No Title"

                # Extract article summary
                summary_element = article.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
                summary = summary_element.get_text(strip=True) if summary_element else "No Summary"

                # Extract article date
                date_str = article.find('time')['datetime']
                article_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').date()

                # Calculate the number of days ago the article was published
                days_ago = (today - article_date).days

                # Display if the article is within the last 5 days
                if days_ago <= 5:
                    print(f"Title: {title}")
                    print(f"Summary: {summary}")
                    print(f"Published {days_ago} days ago\n")

        else:
            print(f"Error: Unable to fetch news. Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

# Get user input for the person's name
person_name = input("Enter the person's name:  ")

# Call the function with the provided name
get_news(person_name)
