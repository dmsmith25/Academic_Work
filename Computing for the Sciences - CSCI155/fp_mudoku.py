"""
CSCI 150 Final Program 1

Name: Dean Smith
Section: V

"""



def print_mudoku(mudoku_list):
    """
    This function takes a parameter of a list for a mudoku and prints out the values
    in the list into a square grid.
    Inputs: mudoku_list (list)
    Return: No value is returned but the mudoku grid is printed in the shell
    """
    
    row = ''
    
    mudoku_length = len(mudoku_list)
    
    for list in mudoku_list: #for each list (row) in the moduku list
        
        counter = 0
        
        for num in list: #for each number within the list (row)
            counter += 1
            if counter == mudoku_length: #if it is the last row
                row += str(num)
            else: #if it is not the last row
                row += str(num) + ' '
            
        print(row)
        row = ''
            
            

def is_mudoku(mudoku_list):
    """
    This function takes a parameter of a list for a mudoku and returns whether or not
    the inputed mudoku list is a valid mudoku.
    Inputs: mudoku_list (list)
    Return: Whether or not list is mudoku (Boolean)
    """
    
    # The valid range of numbers in a mudoku given the size of the list
    ideal_set = set(range(1, len(mudoku_list) + 1))
    
    for row in mudoku_list: #for each list (row) within the mudoku list
        
        # get rid of duplicate values
        row_set = set(row)
        
        if row_set != ideal_set: 
            return False
        
        
        
    for i in range(len(mudoku_list)): #for the amount of rows in the mudoku list
        
        column_set = set()
        
        for n in range(len(mudoku_list)): #for the amount of values in each row/column
            column_set.add(mudoku_list[n][i]) #adds the first value of each row to the coulmn set
            
        if column_set != ideal_set:
            return False
        
    
    return True




def reasons_not_mudoku(mudoku_list):
    """
    This function takes a parameter of a list for a mudoku and prints the reasons why the list is not a moduku.
    If the mudoku is valid, then the function prints nothing.
    Inputs: mudoku_list (list)
    Return: No value is returned but the reasons why the mudoku is not valid are printed into the shell
    """
    
    # The valid range of numbers in a mudoku given the size of the list
    ideal_set = set(range(1, len(mudoku_list) + 1))
        
        
    for row in mudoku_list: #for each row in the list
            
        #gets rid of duplicates
        row_set = set(row)
            
        if row_set != ideal_set:
            if len(row_set) < len(row): #if there was a duplicate
                print('Duplicate values in row ' + str(mudoku_list.index(row) + 1))
                    
            if row_set - ideal_set != set(): #if there are illegal values
                    
                illegal_value = ''
                    
                for num in (row_set - ideal_set):
                    illegal_value += str(num)
                        
                print('Illegal value ' + illegal_value)
                    
                    
                    
    for i in range(len(mudoku_list)): #for the amount of rows
        
        column_set = set()
        
        for n in range(len(mudoku_list)): #for the amount of values in each row/column
            column_set.add(mudoku_list[n][i])
            
        if (column_set != ideal_set) and (column_set - ideal_set == set()): #if the column has a duplicate value
            print('Duplicate values in column ' + str(i + 1))
                


                
                


def check_mudoku(mudoku_list):
    """
    This function uses the 'print_mudoku' function and the 'is_mudoku' function to print and evaluate
    the input mudoku list
    Inputs: mudoku_list(list)
    Return: No value is returned but the mudoku grid is printed along with whether or not it is a valid
            mudoku and the reasons why it isn't a valid mudoku
    """
    
    print_mudoku(mudoku_list)
    if is_mudoku(mudoku_list) == True:
        print('Is a valid mudoku')
    else:
        print('Is NOT a valid mudoku:')
        reasons_not_mudoku(mudoku_list)
    
    
    
        
        
        