#https://github.com/SideekaAyoob/Python_Snake
#to run python try.py
'''from turtle import *

color("red")
forward(50)#steps taken
right(90) #degrees
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

done()
'''



# Import the Turtle Graphics module
import turtle

#gloabl variables
# Define program constants 
#this is for the size of the window
WIDTH = 500
HEIGHT = 500
DELAY = 10  # Milliseconds between screen updates

#function for tutrle to move
def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)  # After `DELAY` milliseconds, call move_turtle() again


# Create a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the window
screen.title("Turtle Animation") #name / title on top
screen.bgcolor("cyan") #changes background of the program
screen.tracer(0)  # Turn off automatic animation // makes it faster

# Create a turtle to do our bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# Set animation in motion
move_turtle()

# Finish nicely
turtle.done()
