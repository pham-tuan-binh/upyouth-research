from .record_utils import *

def is_title_product_engineering(job_title):
    if job_title is None:
        return False
    
    job_title = job_title.lower()

    # Define singular keywords that indicate a job related to product or engineering
    product_engineering_keywords = [
        "engineer",
        "developer",
        "architect",
        "designer",
        "scientist",
        "technician",
        "technologist",
        "specialist"
    ]

    if any(keyword in job_title for keyword in product_engineering_keywords):
        return True
    
    return False

def is_title_biz(job_title):
    if job_title is None:
        return False
    
    job_title = job_title.lower()

    # Define singular keywords that indicate a job related to business, communications, or marketing
    bcm_keywords = [
        "business",
        "marketing",
        "sales",
        "relations",
        "advertising",
        "management",
        "promotion",
        "strategist",
        "branding",
        "digital",
        "content",
        "social media",
        "promotion",
        "event",
    ]

    if any(keyword in job_title for keyword in bcm_keywords):
        return True
    
    return False

def is_title_finance(job_title):
    if job_title is None:
        return False
    
    job_title = job_title.lower()

    # Define singular keywords that indicate a job related to finance
    finance_keywords = [
        "finance",
        "financial",
        "accountant",
        "banker",
        "investment",
        "controller",
        "treasurer",
        "auditor",
        "actuary",
        "tax",
        "advisor",
        "credit",
        "risk",
        "insurance",
        "banking",
        "capital",
        "portfolio",
        "asset",
        "wealth",
        "equity",
        "derivatives",
        "valuation",
        "budget",
        "forex",
        "fintech",
        "economic",
        "compliance",
        "quantitative",
        "financial planning"
    ]

    if any(keyword in job_title for keyword in finance_keywords):
        return True
    
    return False

def is_company_mnc(company):
    if company is None:
        return False
    
    company = company.lower()

    file_path = "../data/companies/mnc_list.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if company.strip() == line.strip():
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False

def is_company_entrepreneurial(company):
    if company is None:
        return False
    
    company = company.lower()

    file_path = "../data/companies/entrepreneurial_list.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if company.strip() == line.strip():
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False

def is_company_national(company):
    if company is None:
        return False
    
    company = company.lower()

    file_path = "../data/companies/national_list.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if company.strip() == line.strip():
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False

def is_title_high_level(job_title):
    if job_title is None:
        return False
    
    job_title = job_title.lower()

    # Define singular keywords that indicate high-level positions
    high_level_keywords = [
        "ceo",
        "cto",
        "cfo",
        "cmo",
        "coo",
        "founder",
        "co-founder",
        "director",
        "chief",
        "president",
        "executive",
        "partner",
        "head",
        "principal",
        "investor"
    ]

    if any(keyword in job_title for keyword in high_level_keywords):
        return True
    
    return False

def is_title_manager(job_title):
    if job_title is None:
        return False
    
    job_title = job_title.lower()

    # Define singular keywords that indicate a job related to management positions
    manager_keywords = [
        "manager",
        "management",
        "supervisor",
        "coordinator",
        "lead",
        "head",
        "administrator",
        "chief",
        "officer",
        "principal",
        "foreman",
        "overseer",
        "controller",
        "organizer",
        "foreperson",
        "administrator",
        "captain",
        "forewoman"
    ]

    if any(keyword in job_title for keyword in manager_keywords):
        return True
    
    return False

def is_title_intern(job_title):
    if job_title is None:
        return False
    
    job_title = job_title.lower()

    # Define singular keywords that indicate an intern position
    intern_keywords = [
        "intern",
        "trainee",
        "apprentice"
    ]

    if any(keyword in job_title for keyword in intern_keywords):
        return True
    
    return False