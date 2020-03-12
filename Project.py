# Project1

import turtle

wn = turtle.Screen()
wn.bgcolor("white")

neo = turtle.Turtle()
neo.shape("turtle")
neo.color("maroon")

while neo.xcor() < 500 and neo.ycor() < 500:
    neo.forward(150)
    neo.right(90)
    neo.backward(60)
    neo.right(50)
wn.exitonclick()