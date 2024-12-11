import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the job listing page (e.g., We Work Remotely)
url = "https://weworkremotely.com/remote-jobs"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract job postings
    jobs = []

    # Each job is in a 'section' with class 'jobs'
    for job_section in soup.find_all('section', class_='jobs'):
        for job_card in job_section.find_all('li', class_='feature'):
            # Extract job title
            job_title = job_card.find('span', class_='title').text.strip()

            # Extract company name
            company_name = job_card.find('span', class_='company').text.strip()

            # Extract job location (if available)
            location_tag = job_card.find('span', class_='region')
            location = location_tag.text.strip() if location_tag else "Remote"

            # Append to the jobs list
            jobs.append({
                'Job Title': job_title,
                'Company': company_name,
                'Location': location
            })

    # Convert to a DataFrame
    df = pd.DataFrame(jobs)

    # Save to CSV
    df.to_csv('job_listings.csv', index=False)
    print("Job listings have been saved to 'job_listings.csv'")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
