"""
Name: Dean Smith
Section: V
CSI 150 Lab 2


 - This program draws a picture of outer space using the turtle module.
 - Use the function generate_picture() with no inputs to draw the picture.
"""

# import turtle functions as t and randint
import turtle as t
from random import randint

# dimensions of screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


# color codes sorted alphabetically
BLACK = 0,0,0
BLUE = 0, 0, 255
DARK_GREY = 112, 120, 165
GREEN = 0, 255, 0
LIGHT_BLUE = 135, 206, 250
LIGHT_GREY = 160, 175, 204
ORANGE = 255, 165, 0
RED = 255, 0 ,0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0


def triangle(x, y, side_length, color):
    """
    Draws an equilateral triangle with a vertical left edge of
    input length at the input corodinates and is filled in with the
    input color
    
    inputs: x coordinate, y coordinate, the length of each side, color
    of triangle
    """
    t.penup()
    t.setposition(x, y)
    t.setheading(90) #north
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    # repeats steps to draw all three edges of triangle
    for i in range(3):
        t.forward(side_length)
        t.right(120) # exterior angle
    t.end_fill()
    t.penup()
    
    
    
def isosceles(x, y, base_length, color):
    """
    Draws an isosceles triangle at the position of x and y
    with the base length as the input and the side
    Inputs: x coordinate, y coordinate, length of base, and color
    """
    t.penup()
    t.setposition(x, y)
    t.setheading(90)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(base_length) # small edge
    t.right(108) # exterior angle of 72
    t.forward(base_length * 1.64) # about proporionatly size difference of base length to side length
    t.right(144) # exterior angle of 36
    t.forward(base_length * 1.64) # about proporionatly size difference of base length to side length
    t.end_fill()
    t.right(108) #exterior angle of 72
    


def polygon(x, y, side_length, side_number, color):
    """
    Draws a polygon a the given x and y coordinates with the
    number of input sides and filled to the input color
    Inputs: x coordinate, y coordinate, length of side, and color
    """
    t.penup()
    t.setposition(x, y)
    t.setheading(90) #north
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    # draws the input number of sides to form a polygon
    for i in range(side_number):
        t.forward(side_length)
        t.right(360/side_number)
    t.end_fill()
    t.penup()
    
    
    
def rectangle(x, y, side_length, side_height, color):
    """
    Draws a rectangle at the input x and y coordinates with the input
    height (horizontal) and length (vertical) and is filled with the input color
    Inputs: x coordinate, y coordinate, length of side (vertical), length of height (horizontal), and color
    """
    t.penup()
    t.setposition(x, y)
    t.setheading(90) 
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(side_length)
        t.right(90)
        t.forward(side_height)
        t.right(90)
    t.end_fill()
        

def add_circles(radius_min, radius_max, num_circles, color):
    """
    Draws an input number of circles randomly placed with an input
    minimum radius and a input maximum radius. Utilizes the
    t.circle function and fills the circles with the input color.
    Inputs: radius minimum, radius maximum, number of circles, color of circles
    """
    # uses for loop to draw the amount of circles in num_circles
    for i in range(num_circles):
        t.penup()
        # sets random position for each circle
        t.setposition(randint(-350, 350), randint(-350, 350))
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        # gives circle random radius based on input range
        t.circle(randint(radius_min, radius_max))
        t.end_fill()
        t.penup()
    

        
        
def add_stars(side_length_min, side_length_max, num_stars, color):
    """
    Draws an input number of stars randomly placed with an input
    minimum star length and a input maximum star length. Utilizes the
    star function and fills the stars with the input color.
    Inputs: star size minimum, star size maximum, number of stars, color of stars
    """
    # uses the star function to draw stars randomly on the 700 by 700 screen
    # uses a for loop to call the star function the amount of times inputed.
    for i in range(num_stars):
        # uses randtint to randomly select the x and y coordinates and the size of each star
        star(randint(-350, 350), randint(-350, 350), randint(side_length_min, side_length_max), color)
        
       

def planet(x, y, radius, color):
    """
    Draws a planet at the given x and y coordinates with the input radius
    using the t.circle function and fills the planet with the input color.
    Inputs: x coordinate, y coordinate, radius of planet, color of planet
    """
    t.penup()
    t.setposition(x, y)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    
def rocketship(x, y, height, width, color):
    """
    Draws a rocketship moving horizontally at the input x and y coordinates
    with a input height (horizontal) and width (vertical) utilizing the
    rectangle, isosceles, window, tail, and flame functions.
    Inputs: x coordinate, y coordinate, height of rocketship (horizontal), length of rocketship (vertical), color of rocketship
    """
    rectangle(x, y, width, height, color)
    isosceles(x + height , y, height // 2, color)
    window(x, y, height, width, height // 6)
    tail(x, y, height, width, color)
    flame(x, y, width)
    
    
def window(x, y, height, width, radius):
    """
    Draws a white window for the rocketship function at the input x and y coordinates with the height and width inputs being relative to
    the rocketship and with an input radius.
    Inputs: x coordinate, y coordinate, height of rocketship, width of rocketship, radius of window.
    """
    t.penup()
    t.setposition(x, y)
    t.forward((height // 4) - radius)
    t.right(90)
    t.forward(width * 1.5)
    t.pendown()
    t.fillcolor(WHITE)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
def tail(x, y, height, width, color):
    """
    Draws a trapizoidal tail for the rocketship at the input x and y coordinates with the height and width inputs being relative
    to the rocketship and filled with the input color (same as the rocketship).
    Inputs: x coordinate, y coordinate, height of rocketship, width of rocketship, color of rocketship
    """
    t.penup()
    t.setposition(x,y)
    t.setheading(240) # for exterior 30 angle on top of tail
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.right(150) # for exterior 150 degree angle on bottom of tail
    t.forward(width * 2.75) # bottom of tail is 2.75 times as big as the length of the rocketship
    t.right(150) # for exterior 150 degree angle on bottom of tail
    t.forward(width) # distance of angled sides
    t.right(30) # for exterior 30 angle on top of tail
    t.forward(width) # distance for angles sides
    t.end_fill()
    
def flame(x, y, width):
    """
    Draws the flames on the bottom of the tail for the rocketship at the input x and y coordinates and with the
    input height and weight.
    Inputs: x coordinate, y coordinate, side length of each flame 
    """
    t.penup()
    t.setposition(x, y + width)
    t.setheading(120) # 30 counter clockwise of north
    t.forward(width) # gets to the top (verticall) of the tail to begin flames
    t.left(90) # 30 degrees counter clockwise of west
    t.pendown()
    t.fillcolor(ORANGE)
    t.begin_fill()
    #for loop is used to a flame 4 times
    for i in range(4):
        #for loop is used to draw a flame
        for x in range(3):
            t.forward((width*2.75) / 4)
            t.left(120)
        t.setheading(270)
        t.forward((width*2.75) / 4)
        t.setheading(210)
    t.end_fill()
    
def moon(x,y, radius):
    """
    Draws a moon at the input x and y coordinates and as big as the input radius
    Inputs: x coordinate, y coordinate, radius of moon
    """
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.fillcolor(LIGHT_GREY)
    t.begin_fill()
    t.circle(radius) # shape of moon
    t.end_fill()
    t.penup()
    t.fillcolor(DARK_GREY)
    t.penup()
    t.setposition(x, y - radius // 4) # position of 1st crater
    t.pendown()
    t.begin_fill()
    t.circle(radius // 4) # draws 1st crater
    t.end_fill()
    t.penup()
    t.setposition(x + radius // 2 + radius // 3, y - radius // 2) #position of 2nd crater
    t.pendown()
    t.begin_fill()
    t.circle(radius // 3) # shape of 2nd crater
    t.end_fill()
    t.penup()
    t.setposition(x, y - radius) # position of 3rd crater
    t.pendown()
    t.begin_fill()
    t.circle(radius // 5) # shape of 3rd crater
    t.end_fill()
        
def star(x, y, side_length, color):
    """
    Draws a star using the polygon function at the input x and y coordinates with a input side length and filled with the input color.
    Inputs: x coordinate, y coordinate, length of each side, color of star
    """
    t.penup()
    t.setposition(x,y)
    t.pendown()
    # uses polygon function to make center or base of star (pentagon)
    polygon(x, y, side_length, 5, color)
    t.left(60)
    # uses for loop to draw 5 equilateral triangles on the sides of the pentagon center
    for i in range(5):
        t.begin_fill()
        # uses for loop to draw 3 sides to each equilateral triangle on the star
        for x in range(3):
            t.forward(side_length)
            t.right(120)
        t.end_fill()
        t.penup()
        t.right(60)
        t.forward(side_length)
        t.right(12)
        t.pendown()
        
        
def earth(x, y, radius):
    """
    Draws the planet earth using the planet, polygon, and triangle function at the input x and y coordinates and uses the input radius
    Inputs: x coordinate, y coordinate, radius of earth
    """
    # uses planet function to draw the shape of earth
    planet(x, y, radius, LIGHT_BLUE)
    # uses polygon function to draw a piece of land in the upper left part of the earth (USA)
    polygon(x, y - radius // 2, radius // 2, 5, GREEN)
    # uses the triangle function to draw a piece of land in the middle left part of the earth (Mexico)
    triangle(x + radius // 2, y - radius, radius // 2, GREEN)
    # uses the triangle function to draw an island on the lower right part of the earth
    triangle(x + radius, y - (radius + radius // 2), radius // 2, GREEN)
    
    
    
def satalite(x, y, side_length):
    """
    Draws a satalite orbiting the earth using the polygon function at the input x and y coordinates with the input side lengths
    Inputs: x cooridnate, y coordinate, side length
    """
    t.penup()
    polygon(x, y, side_length, 4, LIGHT_GREY) # body of satalite
    polygon(x + side_length, y + (side_length // 4), side_length // 2, 4, LIGHT_GREY) # right wing of satalite
    polygon(x - side_length // 2, y + (side_length // 4), side_length // 2, 4, LIGHT_GREY) # left wing of satalite
    t.penup()
    t.setposition(x + (side_length // 2) + (side_length // 4), y + (side_length // 2)) # center light on satalite
    t.fillcolor(YELLOW)
    t.begin_fill()
    t.circle(side_length // 4)
    t.end_fill()
    t.setposition(x + side_length // 2, y + side_length) # antenna on top of satalite
    t.setheading(60)
    t.pendown()
    t.fillcolor(BLUE)
    t.begin_fill()
    # uses for loop to draw each side of equialateral triangle in atenna
    for i in range(3):
        t.forward(side_length // 2)
        t.left(120)
    t.end_fill()
    
def sun (x, y, side_length):
    """
    Draws a sun using the polygon function at the input x and y coordinates and with the input side length
    Inputs: x coordinate, y coordinate, side length
    """
    t.penup()
    t.setposition(x,y)
    polygon(x, y, side_length, 16, ORANGE) # base of sun (16 sides)
    t.pendown()
    t.left(180)
    # uses a for loop to draw all 16 triangles on the ends of the sun
    for i in range(16):
        t.right(120)
        t.begin_fill()
        # uses a for loop to draw every side on each triangle
        for x in range(3):
           t.forward(side_length)
           t.right(120)
        t.end_fill()
        t.left(142.5)
        t.forward(side_length)
        

def meteor (x, y, side_length):
    """
    Draws a pentagon meteor using the polygon function at the input x and y coordinates with the input side length
    Inputs: x coordinate, y coordinate, side length of meteor
    """
    t.penup()
    t.setposition(x, y)
    polygon(x, y, side_length, 5, LIGHT_GREY) # pentagon
    
    
        
        
def generate_picture():
    """
    This function takes no inputs and uses the functions listed above to draw a picture of space outside earth in a 700 by 700 plane
    which includes, stars, earth, the sun, the moon, rocketships, meteors, and a satalite.
    """
    t.speed(0) # fastest speed for turtle
    t.colormode(255) # colors go from 0-255
    t.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0) # sets up loacation (0, 0)
    t.screensize(SCREEN_WIDTH, SCREEN_HEIGHT,) # sets screen dimensions (700, 700)
    t.bgcolor(BLACK) # sets background color (black)
    add_stars(5, 9, 25, WHITE) # scatters 25 white stars using the add_stars function
    rocketship(-40, 0, 50, 25, RED) 
    rocketship(25, -50, 40, 20, GREEN)
    rocketship(50, -225, 40, 20, YELLOW)
    rocketship(-100,-80, 80, 40, BLUE)
    rocketship(-20, -175, 100, 50, LIGHT_BLUE)
    rocketship(150, -100, 60, 30, LIGHT_GREY)
    moon(200, -200, 50)
    earth(-250, 250, 75)
    satalite(-150, 80, 50)
    sun(25, 125, 50)
    meteor(-200, -200, 25)
    meteor(-250, -100, 40)
    meteor(-225, -150, 50)
    meteor(-275, -200, 25)
    meteor(-225, -275, 40)
    meteor(-325, -275, 60)
    t.hideturtle()
    
    
    
