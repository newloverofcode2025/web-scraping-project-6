import requests
from bs4 import BeautifulSoup
import json
import os

# Base URL of the website to scrape
base_url = 'https://example-ecommerce.com/'

# Function to scrape a single product
def scrape_product(url):
    try:
        response = requests.get(url, verify=False)  # Bypass SSL verification
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product details
    title = soup.find('h1', class_='product-title').get_text()
    price = soup.find('span', class_='price').get_text()
    description = soup.find('div', class_='description').get_text()
    image_url = soup.find('img', class_='product-image')['src']

    return {
        'title': title,
        'price': price,
        'description': description,
        'image_url': image_url
    }

# Function to scrape multiple products
def scrape_products(start_page, num_pages):
    products = []
    for i in range(start_page, start_page + num_pages):
        url = f'{base_url}page/{i}/'
        print(f'Scraping page {i}: {url}')
        try:
            response = requests.get(url, verify=False)  # Bypass SSL verification
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        for product in soup.find_all('div', class_='product'):
            product_url = product.find('a')['href']
            product_data = scrape_product(product_url)
            if product_data:
                products.append(product_data)

    return products

# Main function to run the scraper
def main():
    start_page = 1
    num_pages = 5  # Number of pages to scrape
    products = scrape_products(start_page, num_pages)

    # Ensure the data directory exists
    output_dir = '../data'
    os.makedirs(output_dir, exist_ok=True)

    # Save the data to a JSON file
    output_file = os.path.join(output_dir, 'products.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    print(f'Scraping complete. Data saved to {output_file}')

if __name__ == '__main__':
    main()