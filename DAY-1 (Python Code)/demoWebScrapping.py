import requests
from bs4 import BeautifulSoup


url = "https://weworkremotely.com/remote-jobs"
response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    # print("\n--- Page Title ---")
    # print(soup.title.text)

    with open("webpage.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
    print("HTML content saved to 'webpage.html'")


else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")


