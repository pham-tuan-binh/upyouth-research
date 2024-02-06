from .education_utils import *
from .record_utils import *

# ________________________ Education Time Variable ________________________
# Start Year of Earliest Bachelor's Degree
# Return year 
def get_start_year_of_bachelor(founder):
    education_records = founder["education"]

    # Iterate over the education records in reverse order
    for record in reversed(education_records):

        # Check if the record is related to a university or college
        if is_degree_bachelor(record["degree_name"]) or is_school_university(record["school"]):
            
            start_year = get_start_year(record)
            
            if start_year is None:
                continue

            return start_year
        
    return 0

def get_age(founder):
    start = get_start_year_of_bachelor(founder)

    if start == 0:
        return 0
    
    return 2024 - start + 18
# ________________________ University variablle ________________________
# Checked, this means they go to top 200 university in the world, this rating is also affected by location of school.
def go_to_elite_university(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in reversed(education_records):
        if is_elite_university(record["school"]):
            return True
        
    return False
    
# ________________________ Major of study variable ________________________
# !!! Majored in Business for Bachelor's Degree
# Return true/false
def majored_in_business(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in reversed(education_records):
        if is_record_business(record) and is_school_university(record["school"]):
            return True
        
    return False

# !!! Majored in Science or Engineering for Bachelor's Degree
# Return true/false
def majored_in_engineering(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_record_engineering(record) and is_school_university(record["school"]):
            return True
        
    return False

# Completed a Science or Engineering PhD
# Return true/false
def completed_phd(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_degree_phd(record["degree_name"]):
            if get_end_year(record):
                return True
        
    return False

def completed_master(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_degree_master(record["degree_name"]):
            if get_end_year(record):
                return True
        
    return False

def completed_bachelor(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_degree_bachelor(record["degree_name"]) or is_school_university(record["school"]):
            if get_end_year(record):
                return True
            
            if not get_start_year(record):
                return True
    
    return False

# Finished Master in Engineering
def master_in_engineering(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_degree_master(record["degree_name"]) and is_record_engineering(record):
            if get_end_year(record):
                return True
        
    return False

# Finished Master in Business
def master_in_business(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_degree_master(record["degree_name"]) and is_record_business(record):
            if get_end_year(record):
                return True
        
    return False

# Finished Phd in Engineering
def phd_in_engineering(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_degree_phd(record["degree_name"]) and is_record_engineering(record):
            if get_end_year(record):
                return True
        
    return False

# Finished Phd in Business
def phd_in_business(founder):
    education_records = founder["education"]

    # Iterate over the education records
    for record in education_records:
        if is_degree_phd(record["degree_name"]) and is_record_business(record):
            if get_end_year(record):
                return True
        
    return False