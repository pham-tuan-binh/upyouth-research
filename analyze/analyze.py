import os
import json
import pandas as pd
from utils import *

# Define the directory path you want to search
directory = "../data/founders"

founders = []

# Loop through each file in the directory
for filename in sorted(os.listdir(directory)):
    file_path = os.path.join(directory, filename)
    
    # Check if it's a file
    if os.path.isfile(file_path):
        # Open and load the JSON file
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)

                data["csv_founder_name"] = filename.split("@")[0]
                data["csv_company_name"] = filename.split("@")[1][0:-5]

                
                founders.append(data)
                # Print the data, or do whatever processing you need
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file {filename}")  


print("founder_name,startup_name,age,education_score,master_study_count,company_score,times_being_founder")
    
for founder in founders:
    education_score, is_master = get_education_score(founder)
    company_score, is_founder = get_company_score(founder)
    age = estimate_age(founder)

    print(f'{founder["csv_founder_name"]},{founder["csv_company_name"]},{age},{education_score},{is_master},{company_score},{is_founder}')
