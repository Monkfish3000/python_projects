from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput('Place your bet', 'Which turtle will win? Enter a color: ')
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

def start_game():
    position = -100
    for col in colors:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(col)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=position)
        position += 35


start_game()


screen.exitonclick()


