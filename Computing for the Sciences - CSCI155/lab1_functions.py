"""
CSCI 150 Lab 1

Name: Dean Smith
Section: V

Creativity:

 - I made the liters_to_gallons function (Line 117) and used both the
 liters_to_gallons function and the kilometers_to_miles function (Line 88)
 to calculate the mpg_from_metric function (Line 133).
 
 - I made the dollars_to_euros function (Line 58) and used the euros_to_dollars
 function (Line 41) to calculate it.
 
 - I made the simple_conversion_function function (Line 27) for simple conversions
 using rates which multiplies the input value by the input rate. This function is used in the
 euros_to_dollars function, the kilometers_to_miles function, and the
 liters_to_gallons function.

"""

"""
Section 1: Functions that return a value
"""

def simple_conversion_function(value, rate):
    """
    Takes two parameters a value and a conversion rate and
    returns the product of both values
    Input type: int or float
    """
    
    # Calculates the product of the value and the conversion rate
    conversion = value * rate
    
    return conversion



def euros_to_dollars(euros):
    """
    Returns the dollar equivalent of the parameter in Euros,
    assuming an exchange rate of 1 Euro = $1.18
    Input type: int or float
    """
    
    # The rate of exchange for 1 euro to dollars
    euro_exchange_rate = 1.18
     
    # Uses the simple_conversion_function to calculate the conversion of euros to dollars given the conversion rate
    dollar_value_of_euros = simple_conversion_function(euros, euro_exchange_rate)
    
    #returns the input value of euros into dollars
    return dollar_value_of_euros


def dollars_to_euros(dollars):
    """
    Returns the euro equivalent of the parameter dollars,
    assuming the rate of exchange is 0.84
    Input type: int or float
    """
    
    # Calculates the input dollars in euros by using the euros_to_dollars function
    #The 0.711864406779661 is used to make the equation dollars * 0.84 not 1.18 
    euro_value_of_dollars = euros_to_dollars(dollars*0.711864406779661)
    
    return euro_value_of_dollars
    



def welcome():
    """
    Translates the English word 'welcome' to the Spanish
    word 'bienvenidas'
    """
    
    #Spanish translation of 'welcome'
    welcome_in_spanish = 'bienvenidas'
    
    
    #returns the Spanish translation of 'welcome'
    return welcome_in_spanish


def kilometers_to_miles(kilometers):
    """
    Converts the input amount of kilometers into
    miles assuming a conversion rate of 0.621371
    Input type: non-negative int or float
    """
    
    # The conversion rate of 1 kilometer to miles
    conversion_rate_of_kilometers_to_miles = 0.621371
    
    # Uses the simple_conversion_function to calculate the conversion of kilometers to miles given the conversion rate
    kilometers_to_miles_conversion = simple_conversion_function(kilometers, conversion_rate_of_kilometers_to_miles)
    
    # Returns the input value of kilometers in miles
    return kilometers_to_miles_conversion


def celsius_to_fahrenheit(celsius):
    """
    Converts the input amount of celsius into fahrenheit
    Input type: int or float
    """

    # Formula for converting celsius to fahrenheit given the conversion rate
    celsius_to_fahrenheit_conversion = (celsius * (9/5)) + 32
    
    # Returns the input value of celsius in fahrenheit
    return celsius_to_fahrenheit_conversion

def liters_to_gallons(liters):
    """
    Converts liters to gallons assuming conversion rate
    of 0.264172
    Input type: non_negative floats or ints
    """
    
    # Conversion rate for liters to gallons
    conversion_rate_liters_to_gallons = 0.264172
    
    # Uses the simple_conversion_function to calculate the conversion of euros to dollars given the conversion rate
    gallons = simple_conversion_function(liters, conversion_rate_liters_to_gallons)
    
    return gallons


def mpg_from_metric(kilometers, liters):
    """
    Converts from kilometers and liters to miles per gallon
    utilizing the liters_to_gallons function and the
    kilometers_to_miles function
    Input: non-negative values kilometers and liters
    Returns: miles per gallon for the given parameters
    """
    
    # Formula to calculate miles per gallon using the 'kilometers_to_miles' function to calculate miles and liters_to_gallons function to calculate gallons
    miles_per_gallon = kilometers_to_miles(kilometers) / liters_to_gallons(liters)
    
    # Returns the mpg given the kilometers and liters from the input
    return miles_per_gallon


                           
"""
Section 2: Functions that print
"""

def four_fours():
    """
    Prints an arithmetic expression for each value 0..9 using exactly
    four 4s and the operators +, -, *, //, %, **, and parentheses
    """
    print(4+4-4-4, "is 4+4-4-4")  # 0
    print(4-4+4//4, "is 4-4+4//4")  # 1
    print(4//4+4//4, "is 4//4+4//4")  # 2
    print((4*4 - 4) // 4, "is (4*4 - 4) // 4") # 3
    print(((4//4)%4) * 4, "is ((4//4)%4) * 4") # 4
    print((4*4 + 4)//4, "is (4*4 + 4)//4") # 5
    print(((4+4)//4) + 4, "is ((4+4)//4) + 4") # 6
    print(4+4-4//4, "is 4+4-4//4") # 7
    print(4+4-4+4, "is 4+4-4+4") # 8
    print(4+4+(4//4), "is 4+4+(4//4)") # 9
    
    
    

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
    seconds = s % 60                                                            # The leftover
    
    

    print(days, "days")
    print(hours, "hours")
    print(minutes, "minutes")
    print(seconds, "seconds")


