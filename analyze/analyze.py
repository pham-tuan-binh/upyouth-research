import os
import json
import pandas as pd

from variables_calculation.education_pathway import *
from variables_calculation.work_experience_pathway import *
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


# Create an empty DataFrame
education_summary_df = pd.DataFrame()

def convertToNum(bool):
    return 1 if bool else 0

for founder in founders:
    # Collect the education summary for each founder
    data = {
        'Founder': founder['csv_founder_name'], 
        'Company': founder['csv_company_name'],
        'Age': get_age(founder),
        'Went to elite university': convertToNum(go_to_elite_university(founder)),
        'Major in Business': convertToNum(majored_in_business(founder)),
        'Major in Engineering': convertToNum(majored_in_engineering(founder)),
        'Completed Doctor Degree': convertToNum(completed_phd(founder)),
        'Completed Master Degree': convertToNum(completed_master(founder)),
        'Completed Bachelor Degree': convertToNum(completed_bachelor(founder)),
        'Master in Engineering': convertToNum(master_in_engineering(founder)),
        'Master in Business': convertToNum(master_in_business(founder)),
        'Doctor in Engineering': convertToNum(phd_in_engineering(founder)),
        'Doctor in Business': convertToNum(phd_in_business(founder)),
        'Role in Product/Engineering': convertToNum(role_in_product_engineering(founder)),
        'Role in Business/Marketing/Comm': convertToNum(role_in_biz(founder)),
        'Role in Finance': convertToNum(role_in_finance(founder)),
        'Work at MNC': convertToNum(work_at_mnc(founder)),
        'Work at Entrepreneurial Company': convertToNum(work_at_entrepreneurial_company(founder)),
        'Work at National Company': convertToNum(work_at_national_company(founder)),
        'Work at a company': convertToNum(work_at_company(founder)),
        'Work as High Level': convertToNum(work_as_high_level(founder)),
        'Work as Manager': convertToNum(work_as_manager(founder)),
        'Work as Intern': convertToNum(work_as_intern(founder))
    }

    work_at_company(founder)

    education_summary_df = pd.concat([education_summary_df, pd.DataFrame([data])], ignore_index=True)

education_summary_df.to_csv('sample_data.csv', index=False) 

# Display the DataFrame or use it for further analysis
percentage_true = education_summary_df.iloc[:, 3:].mean() * 100
print(percentage_true)
