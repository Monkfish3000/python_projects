from turtle import Turtle, Screen

monk = Turtle()
monk.shape('turtle')
monk.color('DarkSeaGreen')

keep_drawin = True
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        monk.forward(100)
        monk.right(angle)
        num_sides + 1

for num_times in range(3, 8):
    draw_shape(num_times)







screen = Screen()
screen.exitonclick()