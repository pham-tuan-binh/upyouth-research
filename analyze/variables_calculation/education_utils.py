# !!! Check if founders went to a prestigous university
def is_elite_university(school_name):
    file_path = "../data/schools/prestigous_school_list.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if school_name.lower().strip() == line.strip():
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False
    
# check if string is related to engineering [Checked]
def is_string_engineering(string):
    if string is None:
        return False
    
    string = string.lower()

    # Define keywords that indicate a university or college
    engineering_keywords = [
        "engineering",
        "computer",
        "electrical",
        "electronics",
        "mechanical",
        "civil",  # Not explicitly mentioned but a common engineering discipline
        "chemical",
        "software",
        "systems",
        "aerospace",
        "biomedical",
        "industrial",
        "environmental",  # Not explicitly mentioned but a common engineering discipline
        "materials",
        "robotics",
        "telecommunications",
        "informatics",  # Often overlaps with computer and information engineering
        "automation",
        "bioengineering",
        "network",
        "math",
        "physic",
        "information",
        "biology",
        "biotech",
        "tech",
        "comput",
        "natural",
        "construct"
    ]

    if any(keyword in string for keyword in engineering_keywords):
        return True
    
    return False

# check if string is related to business [Checked]
def is_string_business(string):
    if string is None:
        return False
    
    string = string.lower()

    # Define keywords that indicate a university or college
    business_keywords = [
        "business",
        "management",
        "finance",
        "marketing",
        "econo",
        "entrepreneurship",
        "accounting",
        "strateg",
        "operations",
        "supplychain",
        "human",
        "leadership",
        "ethics",
        "law",
        "communication",
        "innovation",
        "negotiation",
        "consulting",
        "planning",
        "analysis",
        "research",
        "relation"
    ]

    if any(keyword in string for keyword in business_keywords):
        return True
    
    return False

# check if record is business
def is_record_business(record):
    return is_string_business(record["degree_name"]) or is_string_business(record["field_of_study"])

# check if record is engineering
def is_record_engineering(record):
    return is_string_engineering(record["degree_name"]) or is_string_engineering(record["field_of_study"])

# check if school is related to university
def is_school_university(school):
    if school is None:
        return False
    
    school = school.lower()

    # Define keywords that indicate a university or college
    university_keywords = ["univer", "college", "institute"]

    if any(keyword in school for keyword in university_keywords):
        return True
    
    return False

# check if degree is bachelor degree
def is_degree_bachelor(degree):
    if degree is None:
        return False
    
    degree = degree.lower()

    bachelor_keywords = [
        "bachelor",
        "ba",
        "b.",
        "bsc",
        "be",
        "bp",
        "bt"
        "graduate",
        "matric",
        "entry",
        "junior",
        "associate",
        "minor",
    ]

    if any(keyword in degree for keyword in bachelor_keywords):
        return True
    
    return False

# check if degree is master degree [Checked]
def is_degree_master(degree): 
    if degree is None:
        return False
    
    degree = degree.lower()

    # Define keywords that indicate a university or college
    master_keywords = [
        "master",
        "msc",  # Shortened form of Master of Science
        "meng",  # Shortened form of Master of Engineering
        "mtech",  # Shortened form of Master of Technology
        "mcom",  # Shortened form of Master of Commerce
        "mba",   # Shortened form of Master of Business Administration
        "mcomp",  # Shortened form of Master of Computing
        "mfa",   # Shortened form of Master of Fine Arts
        "med",   # Shortened form of Master of Education
    ]

    if any(keyword in degree for keyword in master_keywords):
        return True
    
    return False

# check if degree is master degree [Checked]
def is_degree_mba(degree):
    if degree is None:
        return False
    
    degree = degree.lower()

    # Define keywords that indicate a university or college
    master_keywords = [
        "mba",
        "m.b.a",
        "m.ba",
        "business admin" # this is checked further
    ]

    if any(keyword in degree for keyword in master_keywords):
        return True
    
    return False

# check if degree is phd degree [Checked]
def is_degree_phd(degree):
    if degree is None:
        return False
    
    degree = degree.lower()

    # Define keywords that indicate a university or college
    phd_keywords = [
        "phd",
        "dphil",  # Shortened form of Doctor of Philosophy
        "dr",     # Shortened form of Doctor
        "doctor"
    ]

    if any(keyword in degree for keyword in phd_keywords):
        return True
    
    return False