import time

def convert_from_seconds(s):
    """
    Input: non-negative integer representing number of seconds
    Prints: number of days, hours, minutes and seconds
    """
    day_in_seconds = 86400
    hour_in_seconds = 3600
    minute_in_seconds = 60
    
    
    
    days = s // day_in_seconds                                                  # Number of days
    hours = (s % day_in_seconds) // hour_in_seconds                             # Number of hours
    minutes = ((s % day_in_seconds) % hour_in_seconds) // minute_in_seconds     # Number of minutes
    seconds = s % 60
    
    total_time_years = (days / 365.25) + (hours / (24 * 365.25)) + (minutes / (60 * 24 * 365.25)) + (seconds / 360 * 24 * 365.25)
    
    return total_time_years