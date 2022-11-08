"""
This file accumulates calculated temperatures for zipcodes over time and stores
them.

CS150
Name: Dean Smith
Section: V
Creativity:

- Tells user if they entered an invalid zipcode (line 70)
"""

import lab7_weather
import sys
import os
import datetime


   
def get_date():
    """
    This function returns the current date and hour in a string that reads:
    mm-dd-yyyy,hour
    Inputs: None
    """
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year) + ',' + str(now.hour)

def new_date_needed(filename, date):
    """
    This function returns whether or not the file being used in aggregate_temp
    already has a date and time entered that is the same as the one trying to be entered.
    Inputs: filename (str), date(str)
    """
    with open(filename, 'r') as file:
        for line in file:
            if str(date) in str(line): # if the date has already been entered
                return False #there is no new entry needed
            
        return True #there is a new entry needed


def aggregate_temp(filename):
    """
    This function takes a filename as a parameter and sees whether or not the file
    exists or not and will then either append to the file or create the file and enter
    the current date, time, and temperature into the file if not already done so.
    Inputs: filename(str)
    """
    if os.path.exists(filename) == True: # if file exists
        if new_date_needed(filename, get_date()) == True: # if there is no entry with the given date
            with open(filename, 'a') as file:
                #skips line in order to go to next line
                file.write('\n' + get_date() + ',' + str(lab7_weather.get_temperature(sys.argv[2]))) #uses lab7_weather get_temperature function to get temp
            
            
    elif os.path.exists(filename) == False: # if file does not exist
        with open(filename, 'a') as file:
            # no line skip because it starts on the first line
            file.write(get_date() + ',' + str(lab7_weather.get_temperature(sys.argv[2])))
            


def print_usage():
    print('usage: python3 lab7_aggregator.py <file> <zipcode>')
    
    
if __name__ == '__main__': #if not imported
    if len(sys.argv) == 3:
        if len(sys.argv[2]) != 5:
            print('zipcode is invalid')
        else:
            aggregate_temp(sys.argv[1])
    else: #if imported
        print_usage()  

