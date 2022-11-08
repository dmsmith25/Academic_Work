"""
CSCI 150 Lab 5

Name: Dean Smith
Section: V

Creativity:

- Created mode function and included it in data analysis (Line 90)

"""

# TODO: Include your data analyses here
"""
Data file name: 95income.txt
File contained 35326 entries
Max: 304998
Min: -13411
Average: 16974.277925607203
Median: 8929.5
Std. dev: 22838.78036356643
Mode: 20000

Analysis:
This data was collected from the Northeast region of the US from the 1995 cencus.
The data contains the income of each of the 35326 surveyed participants with an average
income of approximately $16974.28 with a standard deviation of approximately $22838.78 and a
median income of $8929.50.
"""

"""
Data file name: Toy_Story_reviews.txt
File contained 2077 entries
Max: 5
Min: 1
Average: 4.146846413095811
Median: 4
Std. dev: 0.8523490842765842
Mode: 4


Data file name: Jumanji_reviews.txt
File contained 701 entries
Max: 5
Min: 1
Average: 3.20114122681883
Median: 3
Std. dev: 0.983172043525109
Mode: 3

Analysis:
This data conatains movie reviews from 1 to 5 of the movies
Jumanji and Toy Story. Toy Story had a higher average of
about 4.15 than Jumanji's 3.20 and had a higher median of 4 than
Jumanji's 3. Therefore, according to the participants, Toy Story
was a better movie than Jumanji. 
"""



from math import sqrt


def median(data):
    """
    This function finds the median of a data list
    Inputs: data (list)
    """
    data = sorted(data)
    if len(data) % 2 != 0: #odd
        return data[len(data) // 2]

    if len(data) % 2 == 0: #even
        return (data[len(data) //2] + data[(len(data) // 2) - 1]) / 2

def standard_deviation(data):
    """
    This function returns the standard deviation using an equation of a
    data list
    Inputs: data (list)
    """
    summation = []
    average = sum(data) / len(data)
    for num in data:
        summation.append((num - average) ** 2)
    answer = sqrt(sum(summation) * (1/(len(data) - 1))) #given equation
    
    return answer

def mode(data):
    """
    This function returns the mode of a data list
    Inputs: data(list)
    """
    data = sorted(data)
    count = 0
    i = 0
    num_prev = data[0]
    modes = []
    for num in data:
        if i + 1 == len(data) or num_prev and num != data[i + 1]: #if last value or number previor and not repeated again
            count = count + 1
            modes.append(count)
            count = 0
        elif num == data[i+1]: #if value is repeated again
            count = count + 1
        else:
            count = 0
            modes.append(count)
                
        i = i + 1
        num_prev = num
    mode = dif_entries(data)[modes.index(max(modes))]
    return mode



def dif_entries(list):
    """
    This function creates a list of all of the numbers in a list without
    repeating them.
    Inputs: list
    """
    num_prev = list[0]
    new_list = [num_prev]
    for num in list:
        if num != num_prev:
            new_list.append(num)
            
        num_prev = num
            
    return new_list



def enteries(list):
    """
    This function returns the number of enteries in a list
    Inputs: list
    """
    return len(list)

def maximum(list):
    """
    This function returns the maximum value in a list
    Inputs: list
    """
    return max(list)

def minimum(list):
    """
    This function returns the minimum value in a list
    Inputs: list
    """
    return min(list)

def average (list):
    """
    This funciton returns the average value in a list
    Inputs: list
    """
    return sum(list) / len(list)

def read_file():
    """
    This funciton prompts the user for a file
    then reads the file and returns the file as a list of values
    Inputs: none
    """
    list = []
    question = input ('Data file name: ')
    with open(question, 'r') as file:
        for line in file:
            list.append(int(line))
            
    return list


def data_analysis():
    """
    This function will prompt the user to enter a text file that
    has one number per line in the script.
    Parameters: none
    """
    list = read_file()
    if len(list) == 0:
        print('File contained 0 entries')
    else:
            
        print('File contained ' + str(enteries(list)) + ' entries')
        print('Max: ' + str(maximum(list)))
        print('Min: ' + str(minimum(list)))
        print('Average: ' + str(average(list)))
        print('Median: ' + str(median(list)))
        print('Std. dev: ' + str(standard_deviation(list)))
        print('Mode: ' + str(mode(list)))
        


def frequencies(data):
    """
    This function will return a list of the numbers in a list and how many times they
    appear in the list.
    Inputs: data (list)
    """
    data = sorted(data)
    count = 0
    i = 0
    num_prev = data[0]
    print('data\tfrequency')
    for num in data:
        if i + 1 == len(data) or num_prev and num != data[i + 1]: #if last value or number previor and not repeated again
            count = count + 1
            print (str(num) + '\t' + str(count))
            count = 0
        elif num == data[i+1]: #if value is repeated again
            count = count + 1
        else:
            print (str(num) + '\t' + str(count))
            count = 0
                
        i = i + 1
        num_prev = num
            
        
        


# Main program that gets executed when program is run
# (Leave this as is, no changes to be made)
if __name__ == '__main__':
    # This invokes the data_analysis function when the program is run
    data_analysis()
