import sys
import urllib.request


def get_temperature(zipcode):
    """
    This function takes a zipcode as a parameter and returns the temperature
    as a float in that zipcode according to the weather.
    Inputs: zipcode (str)
    """
    URL = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',us&APPID=0bc9d8717308e4707db54d686600050b&units=imperial'
    PREFIX = '"temp":'
    
    scraped_temp = 'h'
    with urllib.request.urlopen(URL) as webpage:
        for line in webpage:
            line = line.decode('utf-8', 'ignore')
            start_string = line.find(PREFIX)
            if start_string != -1:
                start_string += len(PREFIX)
                end_string = line.find(',' , start_string)
                scraped_temp = line[start_string:end_string]


    print(scraped_temp)
    return float(scraped_temp)
            
            
        
            
    
def print_usage():
    print('usage: python3 lab7_weather.py <zipcode>')
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_temperature(sys.argv[1])
    else:
        print_usage()  
    