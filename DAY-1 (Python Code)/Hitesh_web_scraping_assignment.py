import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "http://books.toscrape.com/"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract book information
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        availability = book.find('p', class_='instock availability').text.strip()

        books.append({
            'Title': title,
            'Price': price,
            'Availability': availability
        })

    # Save to a CSV file
    df = pd.DataFrame(books)
    df.to_csv('hitesh_sol_assignment.csv', index=False)
    print("Book data has been saved to 'books.csv'")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

