def get_start_year(record):
    if record["starts_at"] is None:
            return None

    starts_at = record["starts_at"]
    
    return starts_at["year"]

def get_end_year(record):
    if record["starts_at"] is None:
        return None

    starts_at = record["starts_at"]
    
    return starts_at["year"]

def get_elapsed_time(record):
    start_year = get_start_year(record)
    end_year = get_end_year(record)

    if start_year is None or end_year is None:
         return None
    
    return end_year - start_year

# Return true if experience is countable (present position, with a start date)
def is_record_counted(record):
    if get_start_year(record) is not None:
        return True
    
    return False