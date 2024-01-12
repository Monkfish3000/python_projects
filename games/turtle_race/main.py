from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
bet = screen.textinput('Place your bet', 'Which turtle will win? Enter a color: ')
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']
all_turtles = []

def start_game():
    position = -100
    for col in colors:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(col)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=position)
        position += 35
        all_turtles.append(new_turtle)


start_game()

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            print(f'And the winner is the {turtle.pencolor()} turtle')
            is_race_on = False
            if turtle.pencolor() == bet:
                print('You Win!')
            else:
                print("You lose!")
        dist = random.randint(0,10)
        turtle.forward(dist)



screen.exitonclick()


