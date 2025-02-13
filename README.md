# Web Scraping Project 6

## Overview
This project demonstrates a web scraping task using Python, requests, and BeautifulSoup. It scrapes product details from an e-commerce site, including titles, prices, descriptions, and images, and saves them to a JSON file. The script also handles pagination to scrape multiple pages.

## Project Structure
web-scraping-project-6/
├── src/
│   └── main.py
├── data/
│   └── products.json
└── README.md

## Dependencies
- Python
- requests
- beautifulsoup4

## Setup
1. Clone the repository.
2. Install the required libraries using `pip install requests beautifulsoup4`.
3. Run the script using `python src/main.py`.

## Usage
- The script scrapes product details from the specified e-commerce site and saves them to `data/products.json`.

## Notes
- Replace the base URL in `main.py` with the e-commerce site you want to scrape.
- Ensure you have permission to scrape the website and comply with its `robots.txt` file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Commit and Push Changes:
Open GitHub Desktop.
Make sure your repository is selected.
Click on "Changes" to see the files you've added.
Write a commit message (e.g., "Initial commit with e-commerce product scraping project").
Click "Commit to main".
Click "Push origin" to push your changes to GitHub.