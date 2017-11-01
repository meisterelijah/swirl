import turtle
from turtle import *

elijah = Turtle()
elijah.color ('black')
jim = Turtle()
jim.color('blue')
colormode(255)
screensize (2000,1500)


def yin(radius, color1, color2):
    jim.width(3)
    jim.color("red", color1)
    jim.begin_fill()
    jim.circle(radius/2., 180)
    jim.circle(radius, 180)
    jim.left(180)
    jim.circle(-radius/2., 180)
    jim.end_fill()
    jim.left(90)
    jim.up()
    jim.forward(radius*0.35)
    jim.right(90)
    jim.down()
    jim.color(color1, color2)
    jim.begin_fill()
    jim.circle(radius*0.15)
    jim.end_fill()
    jim.left(90)
    jim.up()
    jim.backward(radius*0.35)
    jim.down()
    jim.left(90)

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

def draw_spirals():
    while True:
        elijah.left(200)
        draw_spiral()
        right (120)
        break

def spin_yin():
    while True:
        yin(50, 'purple', 'orange')
        break
    
def hype():
    for i in range(2):
        spin_yin()
    

def full_eye():
    draw_spiral()
    draw_spirals()
    
    
speed(speed=0)
draw_eye()
draw_spiral()
left (200)
draw_spirals()
yin(50, 'green', 'yellow')
spin_yin()
hype()
full_eye()
resetscreen()
full_eye()


