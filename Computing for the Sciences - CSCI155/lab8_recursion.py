"""
CSCI 150 Lab 8

Name: Dean Smith
Section: V

Creativity:

- Created rec_count function (line 101)
- Created koch_snowflake function (141)
- Created recursive_circles function (163)
"""

import turtle as t
import sys
from random import randint



def length(list):
    """
    This function takes a list as a parameter and returns
    the length of the list without using the len() function.
    Inputs: list (type: list)
    """
    if list == []: # base case
        return 0
    
    else: # recursive case
        return 1 + length(list[1:])
        
        
        
        
def rec_max(list):
    """
    This function takes a list as a parameter and returns
    the maximum value in the list without using the max() function.
    Inputs: list (type: list)
    """
    if list[0] == list[-1]: #base case
        return list[0]
    
    if list[0] > list[1]: #recursive case 1
        return rec_max([list[0]] + list[2:])
    
    if list[0] < list[1]: #recursive case 2
        return rec_max(list[1:])
        
        
        
        

def replace(text, old_substr, new_substr):
    """
    This function takes a string, an old substring, and a new substring
    and replaces all instances of the old substring in the string with
    the new substring.
    Inputs: text (string), old substring (string), new substring (string)
    """
    
    if (len(text) <= len(old_substr)) and text != old_substr: #base case
        return text
    
    
    if text[0:len(old_substr)] == old_substr: #recursive case 1
        return new_substr + replace(text[len(old_substr):], old_substr, new_substr)
             
        
    else: #recursive case 2
        return text[0] + replace(text[1:], old_substr, new_substr)
    
    


def avoids(word, letters):
    """
    This function takes a word and returns True is the word does
    not contain any of the letters in the input letters and returns
    False if the word contains one or more of the letters in the input
    letters.
    Inputs: word (string), letters (string)
    """
    if word == '' or letters == '': #base case 1
        return True
    
    if letters[0] == word[0]: #base case 2
        return False
    
    if avoids(word[1:], letters) == False: #recursive case 1
        return False
    
    if avoids(word, letters[1:]) == False: #recursive case 2
        return False
    
    else: #base case 3
        return True
    
    

def rec_count(list, object):
    """
    This function takes a list and returns how many times the
    inputed object appears in that list.
    Inputs: list (list), object (type: any)
    """
    if list == []: #base case
        return 0
    
    if list[0] == object: #recursive case 1
        return 1 + rec_count(list[1:], object)
    
    else: #recursive case 2
        return rec_count(list[1:], object)
    
    
    
    
def draw_koch(length, generation):
    """
    This function draws a koch curve with an input generation
    and an input length.
    Inputs: length (int or float), generation (int)
    """
    t.down()
    
    if generation == 0: #base case
        t.forward(length)
        
    if generation > 0: #recursive case
        draw_koch(length/3, generation - 1)
        t.left(60)
        draw_koch(length/3, generation - 1)
        t.right(120)
        draw_koch(length/3, generation - 1)
        t.left(60)
        draw_koch(length/3, generation - 1)
        

        
def koch_snowflake(length, generation, number_snowflakes):
    """
    This function uses the draw_koch function to draw an input number
    of snowflakes in random positions with the color pink, purple, or blue.
    Inputs: length (int or float), generation (int), number of snowflakes (int)
    """
    possible_colors = ['pink', 'mediumpurple', 'lightcyan']
    
    if (number_snowflakes % 2 == 0) or ((number_snowflakes - 1) % 2 == 0): #base case
        t.end_fill()
        t.penup()
        t.setposition(randint(-300, 300), randint(-300, 300))
        t.pendown()
        t.fillcolor(possible_colors[randint(0,2)])
        t.begin_fill()
    
    if number_snowflakes > 0: #recursive case
        draw_koch(length,generation)
        t.right(90)
        koch_snowflake(length,generation, number_snowflakes - 0.25)
    
    
def recursive_circles(radius, num_circles):
    """
    This function draws input num_circles within one another with
    the biggest circle having the input radius to create a tunnel picture.
    Inputs: radius (int or float) , num_circles(int)
    """
    t.penup()
    t.setposition(0, -radius)
    t.pendown()
    
    if num_circles == 1: #base case
        t.circle(radius * (1 / num_circles))
        
    if num_circles > 1: #recursive case
        t.circle(radius * (1 / num_circles))
        recursive_circles(radius, num_circles - 1)
    
        
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        t.tracer(False)  # to show drawing all at once
        t.speed(0)        # to increase speed of the drawing a bit
        length = int(sys.argv[1])
        generation = int(sys.argv[2])
        t.penup(); t.backward(length//2); t.pendown()
        draw_koch(length, generation)
        t.update()
        t.done()
        