import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)

# def rotate():
#     length = 5
#     rotation = 90
#     for i in range(60):
#         square(length, rotation)
#         length += 5
#         t.left(5)




def star(x,y):
    for i in range(5):
        t.forward(x)
        t.right(y)
        t.forward(x)
        t.right(y)
        t.forward(x)
        t.right(y)
        t.forward(x)
        t.right(y)
        t.forward(x)

def rotate():
    length = 5
    rotation = 144
    for i in range(60):
        star(length, rotation)
        length += 5
        t.left(5)
rotate()
