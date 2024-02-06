from .record_utils import *
from .work_experience_utils import *



# ________________________ Role Variable ________________________
def role_in_product_engineering(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records:
        if is_title_product_engineering(record["title"]) and is_record_counted(record):
            return True
    
    return False

def role_in_biz(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records:
        if is_title_biz(record["title"]) and is_record_counted(record):
            return True
    
    return False

def role_in_finance(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records:
        if is_title_finance(record["title"]) and is_record_counted(record):
            return True
    
    return False

# ________________________ Employer Variable ________________________
def work_at_mnc(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records:
        if is_company_mnc(record["company"]) and is_record_counted(record):
            return True
    
    return False

def work_at_entrepreneurial_company(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records:
        if is_company_entrepreneurial(record["company"]) and is_record_counted(record):
            return True
    
    return False

def work_at_national_company(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records:
        if is_company_national(record["company"]) and is_record_counted(record):
            return True
    
    return False

def work_at_company(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records[1:]:
        if is_record_counted(record):
            return True
            
    
    return False

# ________________________ Employer Variable ________________________
def work_as_high_level(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records[2:]:
        if is_title_high_level(record["title"]) and is_record_counted(record):
            return True
    
    return False

def work_as_manager(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records[2:]:
        if is_title_manager(record["title"]) and is_record_counted(record):
            return True
    
    return False

def work_as_intern(founder):
    company_records = founder["experiences"]

    # Iterate over the education records
    for record in company_records:
        if is_title_intern(record["title"]) and is_record_counted(record):
            return True
    
    
    return False