import json
import datetime

def categorize_school(school_name):
    # Read the JSON file
    with open('../data/founders/school_list/output.json', 'r') as json_file:
        categories = json.load(json_file)

    # Search for the school in each category without altering the school name
    for category, schools in categories.items():
        if school_name in schools:
            return category
        
    return "other"

def get_education_score(founder):
    education_records = founder["education"]

    score = 0
    is_master = 0

    for record in education_records:
        school_name = record["school"].lower() if record["school"] is not None else ""
        degree_name = record["degree_name"].lower() if record["degree_name"] is not None else ""
        
        temp_score = 0

        # highly prestigous to unknown
        if categorize_school(school_name) == "5":
            temp_score = 5
        elif categorize_school(school_name) == "4":
            temp_score = 4
        elif categorize_school(school_name) == "3":
            temp_score = 3
        elif categorize_school(school_name) == "2":
            temp_score = 2
        elif categorize_school(school_name) == "1" :
            temp_score = 1

        masters = ["mba", "phd", "master", "msc"]
        if any(keyword in degree_name for keyword in masters):
            is_master += 1

        score = max(score, temp_score)
        
    return [score, is_master]

def categorize_company(company_name):
    # Read the JSON file
    with open('../data/founders/company_list/output.json', 'r') as json_file:
        categories = json.load(json_file)

    # Search for the school in each category without altering the school name
    for category, companies in categories.items():
        if company_name in companies:
            return category
        
    return "other"

def get_company_score(founder):
    company_records = founder["experiences"]

    score = 0
    is_founder = 0

    for record in company_records:
        company_name = record["company"].lower() if record["company"] is not None else ""
        title = record["title"].lower() if record["title"] is not None else ""
        
        temp_score = 0

        # highly prestigous to unknown
        if categorize_company(company_name) == "3":
            temp_score = 3
        elif categorize_company(company_name) == "2":
            temp_score = 2
        elif categorize_company(company_name) == "1" :
            temp_score = 1
        elif categorize_company(company_name) == "0" :
            temp_score = 0

        founders = ["founder", "ceo", "cto", "coo", "exec", "chair"]
        if any(keyword in title for keyword in founders):
            is_founder += 1

        score = max(score, temp_score)
        
    return [score, is_founder]


def estimate_age(founder):
    education_records = founder["education"]

    # Define keywords that indicate a university or college
    university_keywords = ["university", "college", "institute", "bachelor"]

    # Iterate over the education records in reverse order
    for record in reversed(education_records):
        school_name = record["school"].lower() if record["school"] is not None else ""
        degree_name = record["degree_name"].lower() if record["degree_name"] is not None else ""

        if record["starts_at"] is None:
            continue

        starts_at = record["starts_at"]
        

        # Check if the record is related to a university or college
        if any(keyword in school_name for keyword in university_keywords) or \
           any(keyword in degree_name for keyword in university_keywords):
            
            
            start_year = starts_at["year"]

            current_year = datetime.datetime.now().year
            return current_year - start_year + 18

    # Return None if no relevant education record is found
    return 0