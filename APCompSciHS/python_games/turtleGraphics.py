'''
Created on May 18, 2016

@author: 174500
'''
from tkinter import *
import turtle
import random
if __name__ == "__main__":
    def graphics():
        print(1)
        global canvas
        window = Tk()
        canvas = Canvas(window, width=800, height=600)
        canvas.pack()
        
    def hello():
        bob = turtle.Turtle()
        bob.forward(50)
        turtle.done() 
    def color():
        painter = turtle.Turtle()
        """    
        painter.pencolor("blue")
        for i in range(70):
            painter.forward(60)
            painter.left(143)
        painter.pencolor("red")
        for i in range(44):
            painter.forward(130)
            painter.left(88)
        painter.pencolor("blue")
        for i in range(33):
            painter.forward(28)
            painter.left(66)
        painter.pencolor("orange")
        for i in range(28):
            painter.forward(72)
            painter.left(39)
        painter.pencolor("green")
        for i in range(19):
            painter.forward(64)
            painter.left(71)
        painter.pencolor("purple")
        for i in range(34):
            painter.forward(54)
            painter.left(92)
        painter.pencolor("yellow")
        for i in range(66):
            painter.forward(103)
            painter.left(97)
        painter.pencolor("red")
        for i in range(101):
            painter.forward(21)
            painter.left(10) 
        """
        r = "red"
        g = "green"
        b = "blue"
        y = "yellow"
        o = "orange"
        p = "purple"
        v = "violet"
        i = "indigo"
        for i in range(60):
            num = random.randrange(1,50)
            num1 = random.randrange(1,30)
            num2 = random.randrange(1,100)
            colorRand = random.randrange(1,8)
            if colorRand == 1:
                color = r
            elif colorRand == 2:
                color = g
            elif colorRand == 3:
                color = b
            elif colorRand == 4:
                color = y
            elif colorRand == 5:
                color = o
            elif colorRand == 6:
                color = p
            elif colorRand == 7:
                color = v
            elif colorRand == 8:
                color = i
            painter.pencolor(color)
            for i in range(num):
                painter.forward(num1)
                painter.left(num2)
        turtle.done()
    
    color()
    hello()
    graphics()