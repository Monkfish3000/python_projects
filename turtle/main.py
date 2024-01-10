from turtle import Turtle, Screen
import random

monk = Turtle()
monk.shape('turtle')
monk.color('DarkSeaGreen')

colours = ["red", "green", "blue", "orange", "purple", "wheat", "DarkOrchid", "CornflowerBlue"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Convert to 0-1 scale
    rgb = (r / 255, g / 255, b / 255)
    return rgb


directions = [0, 90, 180, 270]
monk.pensize(15)
monk.speed('fastest')

for _ in range(200):
    monk.color(random_color())
    monk.forward(30)
    monk.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()