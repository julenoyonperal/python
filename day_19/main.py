# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:19:04 2021

@author: joyon
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_up():
    tim.forward(1)

def move_down():
    tim.backward(1)
    
def move_left():
    tim.left(1)
    
def move_right():
    tim.right(1)
    
def clean():
    tim.clear()
    
screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clean)
screen.exitonclick()