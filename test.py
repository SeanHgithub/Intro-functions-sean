import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

""" t.forward(200)
def message(input):
    print(input)
message("Hello Class") 
def square(x)    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x) 
square(200)
 def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x) 
 equal(200) 
     def right()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142) 
 def rectangle()
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)  """

""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) """

""" def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right() """

""" def rectangle():
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
rectangle() """

""" def equal():
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal() """
""" for i in range(4):
    print(i)
    t.forward(100)
    t.left(90) """
""" for i in range(100):
    print(i)
    t.left(5)
    for i in range(4):
        print(i)
        t.forward(100)
        t.left(90) """
""" for i in range(3):
    print(i)
    t.forward(100)
    t.left(120) """
""" for square in range(4):
    print(square)
    t.forward(100)
    t.left(90) """
""" x = 100
y = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y) """
""" def doublesquares(iRange):
    length = 25
    for i in range(iRange):
        square(length,90)
        length = length * 2
doublesquares(5)
turtle.done() """
#Strings characters letters
#parenthesis means function
#return is output
#input produces string
#integers or numbers
t.speed(1000)
""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(10,90)
def addSquares(iRange):
    length = 10
    for i in range(iRange):
        square(length,90)
        length = length + 10
addSquares(60)
turtle.done() """
""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(5,90)
def addSquares(iRange):
    length = 10
    for i in range(iRange):
        square(length,90)
        length = length + 5
        t.left(5)
addSquares(60) """
def star(x,y):
    for i in range(5):
        t.forward(x)
        t.right(y)
star(350,144)
def addStars(iRange):
    length = 350
    for i in range(iRange):
        star(length,144)
        t.left(6)
        length = length * 0.995
addStars(100)

turtle.done()