import turtle
from turtle import *

elijah = Turtle()
elijah.color ('black')
jim = Turtle()

def yin(radius, color1, color2):
    width(3)
    color("red", color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()

def draw_spiral():
    elijah.begin_fill()
    elijah.width(2)
    elijah.circle(100/2., 180)
    elijah.circle(100, 180)
    elijah.left(180)
    elijah.circle(-100/2., 180)
    elijah.end_fill()
    elijah.ht()

def draw_eye():
    jim.shape("circle")
    jim.shapesize(21,45,12)
    jim.fillcolor("red")

draw_eye()
draw_spiral()

