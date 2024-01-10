from turtle import Turtle, Screen
import random

monk = Turtle()
monk.shape('turtle')
monk.color('DarkSeaGreen')

colours = ["red", "green", "blue", "orange", "purple", "wheat", "DarkOrchid", "CornflowerBlue"]
directions = [0, 90, 180, 270]
monk.pensize(15)
monk.speed('fastest')

for _ in range(200):
    monk.color(random.choice(colours))
    monk.forward(30)
    monk.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()