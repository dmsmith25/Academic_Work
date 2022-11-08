"""
CSCI 150 Lab 9

Name: Dean Smith
Section: V

Creativity:

- Adds color to H function as it gets bigger (line 95)
- Implements recursive_circles function (line 123)
- Implements challenge_problem_3 function (line 152)

"""

import turtle as t

def gcd(a, b):
    """
    This function takes two integers as parameters and returns the
    greatest common divisor between them.
    Inputs: first integer (int), second integer (int)
    """
    rem = a % b
    if rem == 0: #base case
        return b
    else: #recursive case
        return gcd(b, rem)
        
        
def stairs(length, levels):
    """
    This function creates a drawing a input level amount of steps
    with the biggest one being input length long while the rest get
    exponentially smaller.
    Inputs: length (int or float), levels (int)
    """
    if levels == 0: #base case
        pass
        
        
    else: #recrusive case
        t.forward(length)
        t.right(90)
        t.forward(length)
        t.left(90)
        stairs(length/2, levels - 1)
        t.back(length)
        t.right(90)
        t.back(length)
        t.left(90)
        
    

def sierpinski(length, iterations):
    """
    This function draws a sierpinski triangle of input length with
    input iterations
    Inputs: length (int or float), iterations (int)
    """
    if iterations == 1: #base case
        t.forward(length)
        t.left(120)
        t.forward(length)
        t.left(120)
        t.forward(length)
        t.left(120)
        
    else: #recursive case
        sierpinski(length / 2, iterations - 1)
        t.forward(length)
        t.left(120)
        sierpinski(length / 2, iterations - 1)
        t.forward(length)
        t.left(120)
        sierpinski(length / 2, iterations - 1)
        t.forward(length)
        t.left(120)
        


def recursive_H(length, level):
    """
    This function makes a web of H's with dots at the end of them with
    an input length and an input number of levels.
    Inputs: length (int or float), level (int)
    """
    # In order to change color as web gets bigger
    t.colormode(255)
    
    
    if level == 0: #base case
        t.dot()
        
    else: #recursive case
        t.pencolor(255, 255 // (level * 2), 255 // (level ** 2)) #creativity
        t.forward(length)
        t.left(90)
        t.forward(length / 2)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.back(length)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.forward(length / 2)
        t.left(90)
        t.forward(length * 2)
        t.right(90)
        t.forward(length / 2)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.back(length)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.forward(length / 2)
        t.right(90)
        t.forward(length)


def recursive_circles(radius=150, level=3):
    """
    This function makes circles within one another with an input radius
    and input number of levels
    Inputs: radius (int or float) , level (int)
    """
    if level == 0: #base case
        pass
        
    else: #recursive case
        t.circle(radius)
        t.circle(radius / 2)
        t.penup()
        t.left(90)
        t.forward(radius)
        t.right(90)
        t.pendown()
        t.circle(radius / 2)
        recursive_circles(radius / 2, level - 1)
        t.penup()
        t.right(90)
        t.forward(radius)
        t.left(90)
        t.pendown()
        recursive_circles(radius / 2, level - 1)
        
        
        
        
def challenge_problem_3(length=200, iterations=4):
    """
    This function draws a sierpinski triangle but with squares.
    Inputs: length (int or float), iterations (int)
    """
    t.pencolor('white')
    t.fillcolor('black')
    
    if iterations == 1: #base case
        t.begin_fill()
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.end_fill()
        
    else: #recursive case
        challenge_problem_3(length / 3, iterations - 1)
        t.forward(length / 3)
        challenge_problem_3(length / 3, iterations - 1)
        t.forward(length / 3)
        challenge_problem_3(length / 3, iterations - 1)
        t.right(90)
        t.forward(length / 3)
        t.left(90)
        challenge_problem_3(length / 3, iterations - 1)
        t.right(90)
        t.forward(length / 3)
        t.left(90)
        challenge_problem_3(length / 3, iterations - 1)
        t.back(length / 3)
        challenge_problem_3(length / 3, iterations - 1)
        t.back(length / 3)
        challenge_problem_3(length / 3, iterations - 1)
        t.left(90)
        t.forward(length / 3)
        t.right(90)
        challenge_problem_3(length / 3, iterations - 1)
        t.left(90)
        t.forward(length / 3)
        t.right(90)
    
    
    
# Testing code is provided below that calls the recursive functions above
        
def stairs_demo(length=256, levels=5):
    """
    Set up for stairs drawing and call stairs().

    First moves the turtle to the top left of the screen, then calls stairs()  
    to draw a staircase of squares. Calls turtle.done() at the end of drawing.
    
    Args:
        length: side length of top square in pixels 
        levels: number of boxes to draw 
    """
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    t.penup()
    t.goto(-t.window_width()/2 + 20, t.window_height()/2 - 20)
    t.pendown()    

    # draw the stairs by calling recursive function
    stairs(length, levels)

    # finished
    t.done()


def sierpinski_demo(length=300, iterations=5):
    """
    Set up for sierpinski drawing and call sierpinski().
    
    First moves the turtle to the left edge of the drawing window, turns off
    tracer, and then calls sierpinski(). Calls turtle.done() at end of drawing.
    
    Args:
        length: base length of Sierpinski triangle in pixels 
        iterations: complexity level of Sierpinski triangle 
    """
    if iterations > 3:
        # turn off animation (too slow for high iterations)
        t.tracer(False)
    
    # pick up the pen and move the turtle so it starts at the left edge of the canvas
    t.penup()
    t.goto(-t.window_width()/3 + 20,0)
    t.pendown()
    
    sierpinski(length, iterations)
    
    # finish
    t.update()   # need t.update() if using t.tracer(False)
    t.done()     
    

def recursive_H_demo(length=150, level=3):
    """
    Set up for recursive_H drawing and call recursive_H().
    
    Turns tracer off, calls recursive_H(), and ends with turtle.done().
    
    Args:
        length: height of innermost H in pixels
        level: complexity level of recursive H
    """
    if level > 2:
        # turn off animation (too slow for high iterations)
        t.tracer(False)
    
    recursive_H(length, level)
    
    t.update()    # need t.update() if using t.tracer(False)
    t.done()
    

def drawing_demo():
    """
    Create drawings of `stairs`, `sierpinski`, and `recursive_H`.
    
    Args:
        None
    """
    t.tracer(False)
    
    # draw stairs in upper left of drawing window
    t.penup()
    t.goto(-t.window_width()/2 + 20, t.window_height()/2 - 20)
    t.pendown()    
    stairs(150, 6)
       
    # draw sierpinski in upper right of drawing window
    t.penup()
    t.goto(0, t.window_height()/2 - 300)
    # t.goto(0,40)
    t.pendown()    
    sierpinski(300, 5)
    
    # draw recursive H in lower half of drawing window
    t.penup()
    t.goto(0, -t.window_height()/4)
    t.pendown()    
    recursive_H(150, 4)
    
    # finish
    t.update() 
    t.done()     
