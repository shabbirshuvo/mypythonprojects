# this is a simple code experiment
# used turtle graphics library to draw circles

# importing libraries
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()  # initialize the turtle
t.colormode(255)  # set color mode of the turtle graphics to RGB
tim.hideturtle()  # hide the tutle for better presentation


def random_color():
    # this function generates random values of RGB color
    # then returns value of the color
    # the max limit is 255 because this is the maximum value of RGB
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    choice_color = (r, g, b)
    return choice_color


move_list = [0, 180, 90, 270]  # give the angle of moves
walk_distance = 30  # give the distance of the moves
number_of_walks = 200
# tim.pensize(10)
tim.speed(20)  # increase speed to speed up drawing
tim.setheading(0)  # set the starting point of the turtle
size_of_the_gap = 5  # value of incremental change of the angle
for i in range(int(360 / size_of_the_gap)):
    color_rgb = random_color()
    tim.color(color_rgb)
    tim.circle(100)  # radius  of the circle
    tim.setheading(tim.heading() + size_of_the_gap)  # change the heading incrementally

screen = t.Screen()
screen.exitonclick()

# move_towards = random.choice(move_list)
# tim.setheading(move_towards)
# tim.forward(walk_distance)
