#!/usr/bin/python3
#REF: TechwithTim Youtube
import turtle
from turtle import Turtle, Screen

screen = Screen()
t = Turtle("turtle")
t.speed(-1)

def drag(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))   #x and y is where the mouse is
    t.goto(x, y)   #go to x and y
    t.ondrag(drag)   #keeps calling drag if moving

def clickright(x, y):   #originally didn't have x and y variables and didn't work
    t.clear()   #clears screen if right click

def main():
    turtle.listen()
    t.ondrag(drag)
    turtle.onscreenclick(clickright, 3)
    screen.mainloop()

main()      #calling main function
