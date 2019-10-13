
#import turtle

#t = turtle.Pen()

#turtle.bgcolor("black")

#colors = ["red", "yellow", "blue", "green"]

#for x in range(100):
#    t.pencolor(colors[x%4])
#    t.circle(x)
#    t.left(91)

import turtle
t=turtle.Pen()
turtle.bgcolor("white")
colors=["red","yellow","gray","orange"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)