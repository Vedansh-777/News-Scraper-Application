# News Scraper Application

## Introduction

The News Scraper is a web application designed to fetch and display news articles related to a specific person. It uses Google News as a source and provides a user-friendly interface to view the latest articles within the last 5 days.

## Features

- Fetches and displays news articles related to a specified person.
- Filters articles to show only those published in the last 5 days.
- Provides article details, including title, summary, and days ago.

## Snapshots
<img width="1262" alt="News_Scraper_1" src="https://github.com/Vedansh-777/News-Scraper-Application/assets/86073818/1139de73-9d20-40f4-b635-1957c05752ac">
<img width="1792" alt="News_Scraper_2" src="https://github.com/Vedansh-777/News-Scraper-Application/assets/86073818/62174971-5b0f-4352-96c3-e2e6e1cd4aaf">


## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the Repository to your local machine:

    ```shell
    git clone https://github.com/Vedansh-777/News-Scraper-Application.git
    ```

2. Navigate to the project directory:

    ```shell
    cd news_scraper
    ```

3. Install dependencies:

    ```shell
    pip install django
    ```
    ```shell
    pip install -r requirements.txt
    ```
    ```shell
    pip install requests
    ```
    ```shell
    pip install bs4 
    ```
    Extra setup work
    * Set ```DEBUG=True``` if necessary
    * Add ```127.0.0.1``` to ```ALLOWED_HOSTS```

  4. Run Django Server: 
     ```shell
     python manage.py runserver
     ```
Now you can access the website at ```127.0.0.1:8000```.


### Usage

1. Run the application:

    ```shell
    python news_scraper.py
    ```

2. Open your web browser and visit http://127.0.0.1:5000.

3. Enter the person's name when prompted.

4. View the latest news articles related to the specified person.

## Contributing

We welcome contributions from the community. Whether you want to report a bug, suggest an enhancement, or contribute code, please follow the guidelines [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to reach out if you have any questions or need further assistance. Enjoy using the News Scraper application!








