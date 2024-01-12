from turtle import Turtle, Screen

monk = Turtle()
screen = Screen()

def move_fowards():
    monk.forward(10)


screen.listen()
screen.onkey(move_fowards, 'space')
screen.exitonclick()