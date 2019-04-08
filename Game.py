#https://codeclubprojects.org/en-GB/python/turtle-race/
from turtle import *
from random import randint
import random

global placex, placey 
placex=-150
placey=100

#-------------------class-------------------
class arryOFTurtle(object):
    def __init__(self, number):
        self.number = number

#------------------func---------------------
def CreateTurtle(color):
    t=Turtle()
    global placex,placey
    t.color(color)
    t.shape('turtle')
    t.penup()                    # Pull the pen up -- no drawing when moving
    t.goto(placex,placey)        # Move turtle to an absolute position.
    t.pendown()                  # Pull the pen down -- drawing when moving.
    placey=placey-30   
    return t


def CreateRace():
    penup()
    speed(50)
    goto(-140,140)
    for step in range(16):
        write(step)
        #------
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        #------
        forward(20)



#------------------Main---------------------
color=["red","blue","green","black","pink"]
arryOFTurtle=[]

amountPlayer=int(input("how many player?"))
for x in range(amountPlayer):
    colorChoices=int(input("what color you what? 1)red 2)blue 3)green 4)black 5)pink\n"))
    t=CreateTurtle(color[colorChoices-1])
    arryOFTurtle.append(t)



CreateRace()
#Move the turtle forward by the specified distance.
forward(20)
for turn in range(100):
    for obj in arryOFTurtle:
        obj.forward(randint(1,7))

mainloop()
