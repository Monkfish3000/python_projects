from turtle import Turtle, Screen

monk = Turtle()
screen = Screen()

def move_fowards():
    monk.forward(10)

def move_backwards():
    monk.backward(10)

def turn_right():
    monk.right(10)

def turn_left():
    monk.left(10)

def clear():
    monk.clear()
    monk.penup()
    monk.home()
    monk.pendown()


screen.listen()

screen.onkey(move_fowards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')

screen.onkey(clear, 'c')

screen.exitonclick()