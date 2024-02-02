import pandas as pd
import requests
import json

# Function to call the URL and save JSON to a file
def get_linkedin(linkedin):
    # Make a GET request to the URL
    api_key = 'vNoEuJEYdYEuEGUvkcHpfQ'
    headers = {'Authorization': 'Bearer ' + api_key}

    url = "https://nubela.co/proxycurl/api/v2/linkedin"

    response = requests.get(url,
                        params={'linkedin_profile_url': linkedin},
                        headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        return response.json()
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")

def save_to_json(data, filename):
    # Save the JSON data to a file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"JSON data saved to {filename}")


def save_linkedin(url, filename):
    data = get_linkedin(url)
    save_to_json(data, filename)

# Path to your CSV file
csv_file_path = '../data/founders_linkedin.csv'

# Load the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Loop through each row in the DataFrame
for index, row in data.iterrows():
    # Accessing data from each column
    name = row['Name']
    company = row['Company']
    linkedin = row['Linkedin']

    file_name = f"{name.casefold().replace(' ', '_')}@{company.casefold().replace(' ', '_')}.json"
    
    save_linkedin(linkedin, f"./json/{file_name}")

    # Example operation: printing the values
    print(f"Row {index}: {file_name}")