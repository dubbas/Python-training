"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi),pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if(i<50):
    print("i is less than 50")
elif(i>50):
    print("i is greater than 50")



# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print("My fruit is",picked_fruit)
if(picked_fruit=="orange"):
    print("colour of my fruit is Orange")
elif(picked_fruit=="Strawberry"):
    print("colour of my fruit is Red")
elif(picked_fruit=="banana"):
    print("colour of my fruit is Yellow")



# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
x=int(input("Enter value of x="))
y=int(input("Enter value of y="))
def add(x ,y):
    result=x+y
    return result
print("Addition of x and y=",add(x,y))


# TODO: Now call the function a few times to calculate the following answers
def x(a, b):
    value = a*b
    return value
print("10 x 2 =", x(10,2))

print("4 x 3 =", x(4,3))

print("2 x 3 =", x(2,3))
