"""
CSCI 150 Lab 4

Name: 
Section: 

Creativity:

- Parentheses around pairs of numbers in random_equation
- Advice to user in query_equation
- Prompts user with difficulty in main function

"""

import time
from random import randint

OPERATORS = '+-*'

# Function definitions for math wiz

def random_equation(n):
    """
    This function generates a random equation with the input
    n number of operators(+, -, or *).
    Inputs: number of operators (int)
    """
    # Defines equation with starting parenthese and random number
    # between 1 and 10
    equation = '(' + str(randint(1, 10))
    # For loop is used to add an operator and number to the equation
    # for n number of times
    for i in range(0,n):
        # Adds a random operator to the equation
        equation = equation + str(OPERATORS[randint(0,2)])
        # If the operator added above comes after an end parentheses
        # then a start parentheses is added after the operator
        if (i + 1) % 2 == 0:
            equation = equation + '('
        # Adds number to equation
        equation = equation + str(randint(1, 10))
        # If the number added above comes at the end of a grouping
        # of integers, then an end parentheses is added
        if (i + 1) % 2 != 0:
            equation = equation + ')'
        # If the number added above is the last number of the equation
        # then an end parentheses is added
        if i == n - 1 and i % 2 != 0:
            equation = equation + ')'
        
        
    
    return equation

def query_equation(equation):
    """
    This function prompts the user to answer an input equation.
    The user will be told where the answer is relative to the number
    they answered until they type the correct answer.
    Inputs: equation (string)
    """
    # Define answer as equal to the integer of the response
    # of the user
    answer = int(input (equation + ' = '))
    # Define goal as the correct answer
    goal = eval(equation)
    # Use while loop for while the answer the user gives is not
    # the correct answer, the equation will be asked again until
    # the user gives the correct answer
    while answer != goal:
        if answer >= (goal - 2) and answer <= (goal + 2):
            print('Close, try again!')
        # If the answer is lower than the correct answer then the
        # user is told to guess a higher number.
        elif answer < goal:
            print('Higher!')
        # If the answer is higher than the correct answer then the
        # user is told to guess a lower number.
        elif answer > goal:
            print('Lower!')
        answer = int(input (equation + ' = '))
        
    # Once they answer correctly to get out of the while loop
    print ('Correct!')


def play_game(num_seconds, num_ops):
    """
    This function will prompt the user to solve an equation
    and will count the amount of equations the user gets right
    in the input number of seconds 
    """
    seconds = 0
    start_time = time.time()
    i = 0
    while seconds - start_time < num_seconds:
        query_equation(random_equation(num_ops))
        i = i + 1
        seconds = time.time()
    
    print ('You got ' + str(i) + ' correct in ' + str(seconds - start_time) + ' seconds.')


def main():
    """
    Launch the math wiz game by asking user if they want to play.
    If yes, ask for how long, and play until time is elapsed.
    If no, give a goodbye message.
    Inputs: none
    """
    question = input ('Do you want to play a game? ')
    if question == 'yes':
        duration = input('How long do you want to play for?(seconds) ')
        difficulty = input ('At which difficulty? (number of operators) ')
        # Calls play_game function to start game with inputs from
        # answers given from user
        play_game(int(duration), int(difficulty))
    else:
        print('Have a nice day!')
    

# Main program will be launched automatically when program is run
if __name__ == '__main__':
    main()

