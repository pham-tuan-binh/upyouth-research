import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# scrape yc company website

def find_owners_and_links(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the content with Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links containing 'linkedin'
        linkedin_links = soup.find_all('a', href=lambda href: href and 'linkedin' in href)

        # Map to store owner names and their links
        owner_links_map = {}

        for link in linkedin_links[0:-1]:
            # Navigate to the parent of the parent of the link
            grandparent = link.parent.parent
            parent = link.parent
            # Find the div containing the owner's name
            owner_name_div = grandparent.find('div')
            if owner_name_div:
                owner_name = owner_name_div.get_text(strip=True)

                # Find all links in the grandparent container
                all_links = [a['href'] for a in parent.find_all('a', href=True)]

                # Add or update the owner and their links in the map
                if owner_name in owner_links_map:
                    owner_links_map[owner_name].update(all_links)
                else:
                    owner_links_map[owner_name] = set(all_links)

        return owner_links_map  
    except requests.RequestException as e:
        return f"Error: {e}"

def process_csv_and_scrape(file_path):
    # Read CSV file
    df = pd.read_csv(file_path)

    # Dictionary to store company names and their scraped data
    company_data = {}

    for index, row in df.iterrows():
        yc_link = row['YC Link']
        company_name = row['Company Name']

        # Scrape the YC Link
        scraped_data = find_owners_and_links(yc_link)

        # Convert sets to lists for JSON serialization
        for owner in scraped_data:
            scraped_data[owner] = list(scraped_data[owner])

        # Append the scraped data to the map with the company name as the key
        company_data[company_name] = scraped_data

    return company_data

# Example usage
data = process_csv_and_scrape("./list_of_yc_companies.csv")

for company, links in data.items():
    print(f"Company: {company}\nScraped Data: {links}\n")

json_output_path = "./founders_data.json"
with open(json_output_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
