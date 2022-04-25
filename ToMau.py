import turtle
import random
number = random.uniform (0, 3)
intNumber = int (number)
if intNumber < 1:
    color = "red"
elif intNumber < 2:
    color = "blue"
else:
    color = "yellow"
screen = turtle.Screen ()
screen.title ("Circle")
screen.setup (500, 500)
screen.bgcolor ("black")
t = turtle.Turtle ()
t.color (color)
t.shape ("circle")
t.shapesize (10)
turtle.done ()
