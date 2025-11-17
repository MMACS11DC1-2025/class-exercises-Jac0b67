# Fractal art generator
# Author: Jacob Joe
# Date: November 14, 2025
# A fractal art generator that uses recursion to generate patterns


import turtle  # Imports the turtle module
t = turtle.Turtle()  # Creates a turtle instance

# Recursive function that draws a pattern
def draw_pattern(level, branch_length):
    if level > 0:
        t.forward(branch_length)  # draws the current branch
        t.left(120)
        draw_pattern(level - 1, branch_length / 1.61)

        t.left(120)
        draw_pattern(level - 1, branch_length / 1.61)

        t.left(120)
        draw_pattern(level - 1, branch_length / 1.61)
        t.back(branch_length)
        

t.speed(100) # Sets up the turtle position
t.penup()
t.goto(0, 0)
t.left(90)
t.pendown()

t.color("white") # Sets up the colour and width of turtle
t.width(2)

done = False

while not done:
  level = float(input("How many levels do you want to draw from 1-9? "))
  if level > 9:
    user_input = input("Levels requested are too high, do you want to input a value lower than 9? If not, go autmomatically with 6.(Y/N)").lower()
    if user_input == "n":
      print("Setting to 6 levels.")
      level = 6
      done = True
  elif level <= 0:
    user_input = input("Levels requested are too low, do you want to input a value higher than 0? If not, go automatically with 6.(Y/N)").lower()
    if user_input == "n":
      print("Setting to 6 levels.")
      level = 6
      done = True
  else:
    done = True

  

colors = ["indigo", "purple", "blue", "cyan", "light blue", "white"]

for i in range(8):
    t.pencolor(colors[i % 6])
    draw_pattern(int(level), 60)
    t.right(45)

turtle.done()
