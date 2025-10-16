"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""
# Interactive drawing exercise 
# Author: Jacob Joe
# Date: 10/16/2025

# Imports the turtle
import turtle
bob = turtle.Turtle()

# Defines the circle drawing function
import turtle
bob = turtle.Turtle()

def draw_circle(x, y):
    bob.speed(10)
    bob.penup()
    bob.goto(0 + x, 0 + y)
    bob.pendown()
    bob.circle(50)
    bob.penup()
    bob.goto(-100 + x,0 + y)
    bob.pendown()
    bob.circle(50)
    bob.penup()
    bob.goto(100 + x,0 + y)
    bob.pendown()
    bob.circle(50)
    bob.penup()
    bob.goto(200 + x,0 + y)
    bob.pendown()
    bob.circle(50)
while True: 
    command = input("Do you want to draw the audi logo? (y/n): ").strip().lower()
    if command == 'y':
        draw_circle(-40,0)
        draw_circle(-40,-200)
    elif command == 'n':
        print("Exiting the drawing program.")
        break
    elif command == '67':
        bob.pendown()
        for i in range(4):
          bob.forward(20)
          bob.left(90)
        bob.left(90)
        bob.forward(60)
        bob.right(90)
        bob.forward(20)
        bob.penup()
        bob.goto(60, 0)
        bob.pendown()
        bob.left(90)
        bob.forward(60)
        bob.left(90)
        bob.forward(20)
    else:
       print("Please enter again.")

