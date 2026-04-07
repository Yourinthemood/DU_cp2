import datetime

def get_current_time():
    """Gets the current time and formats it like: 2026-02-18 14:30:22"""
    now = datetime.datetime.now()
    
    # Format: YYYY-MM-DD HH:MM:SS
    # Example: 2026-02-18 14:30:22
    year = now.year
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    
    return f"{year}-{month}-{day} {hour}:{minute}:{second}"

def get_simple_time():
    """Alternative time format if needed"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
