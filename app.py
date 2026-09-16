# import turtle
# from turtle import *
# t = Turtle()

# t.shape('turtle')

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




# def star(x,y):
#     for i in range(5):
#         t.forward(x)
#         t.right(y)
#         t.forward(x)
#         t.right(y)
#         t.forward(x)
#         t.right(y)
#         t.forward(x)
#         t.right(y)
#         t.forward(x)

# star(100,144)

# def rotate():
#     length = 5
#     rotation = 144
#     for i in range(60):
#         star(length, rotation)
#         length += 5
#         t.left(5)
# rotate()


def trees():
    treelength = input()
    trees = list(input().split())
    greater = 0
    greatersample = 1
    lesser = 0
    lessersample = 1

    for i in range(len(trees)):
        
        if trees[i] > trees[i-1]:
            greatersample += 1  
        if greatersample > greater:
            greater = greatersample
        else:
            greatersample = 1
        if trees[i] < trees[i-1]:
            lessersample += 1
        if lessersample > lesser:
            lesser = lessersample
        else:
            lessersample = 1
    print(greater)
    print(lesser)
trees()