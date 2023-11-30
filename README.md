# News-Scraper-Application

## Introduction

The News Scraper is a web application designed to fetch and display news articles related to a specific person. It uses Google News as a source and provides a user-friendly interface to view the latest articles within the last 5 days.

## Features

- Fetches and displays news articles related to a specified person.
- Filters articles to show only those published in the last 5 days.
- Provides article details, including title, summary, and days ago.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the Repository to your local machine:

    ```shell
    git clone (https://github.com/Vedansh-777/News-Scraper-Application.git)
    ```

2. Navigate to the project directory:

    ```shell
    cd news_scraper
    ```

3. Install dependencies:

    ```shell
    pip install -r requirements.txt
    ```

### Usage

1. Run the application:

    ```shell
    python app.py
    ```

2. Open your web browser and visit http://127.0.0.1:5000.

3. Enter the person's name when prompted.

4. View the latest news articles related to the specified person.

## Library Usage

This project utilizes the following Python libraries:

- **requests**: Used for making HTTP requests to fetch news articles from Google News.

- **BeautifulSoup**: A library for pulling data out of HTML and XML files. In this project, it is used for parsing the HTML content of the news articles.

- **datetime**: Used for working with dates and times. It helps in calculating the publication date of news articles.

- **re**: The regular expressions module is used for pattern matching in this project.

- **Django**: If you are using Django for your project, it is a high-level Python web framework. Make sure to follow Django-specific instructions for setting up and running the project locally.

Make sure to install these libraries before running the project. 

## Contributing

We welcome contributions from the community. Whether you want to report a bug, suggest an enhancement, or contribute code, please follow the guidelines [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to reach out if you have any questions or need further assistance. Enjoy using the News Scraper application!
