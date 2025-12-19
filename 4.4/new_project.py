# Fractal art generator
# Author: Jacob Joe
# Date: November 14, 2025
# A fractal art generator that uses recursion to generate patterns, counts the number of recurisve 
# function calls executed, and allows the user to select the colour pallete if they so desire


import turtle  # Imports the turtle module
t = turtle.Turtle()  # Creates a turtle instance

# A dictionary that allows for easy access of elements 
fractal_settings_dictonary = { "branch_length": 60,  "angle": 120,  "colours": [], "level_cap": 9, "call_count": 0   }

# Recursive function that draws a pattern 
def draw_pattern(level, branch_length):
    fractal_settings_dictonary["call_count"] += 1
    if level > 0:
        t.forward(branch_length)  # draws the current branch
        t.left(fractal_settings_dictonary["angle"])
        draw_pattern(level - 1, branch_length / 1.61)

        t.left(fractal_settings_dictonary["angle"])
        draw_pattern(level - 1, branch_length / 1.61)

        t.left(fractal_settings_dictonary["angle"])
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

# A while loop that will keep requesting the amount of levels until the user inputs an acceptable amount
while not done:
  level = float(input("How many levels do you want to draw from 1-9? "))
  if level > fractal_settings_dictonary["level_cap"]:
    user_input = input("Levels requested are too high, do you want to input a value lower than 9? If not, go autmomatically with 6.(Y/N)").lower()
# Uses default levels if the user does not want to input anything new
    if user_input == "n":
      print("Setting to 6 levels.")
      level = 6
      done = True
# Will ask for another input if user input is less than or equal to 0
  elif level <= 0:
    user_input = input("Levels requested are too low, do you want to input a value higher than 0? If not, go automatically with 6.(Y/N)").lower()
# Uses default levels if the user does not want to input anything new
    if user_input == "n":
      print("Setting to 6 levels.")
      level = 6
      done = True
  else:
    done = True

# Lets user customize the colours
# Can input colours such as blue or light blue
custom_colours = input("Enter up to 9 different comma-split colours for the pattern or press enter to go with defalut option. ").lower()
if custom_colours.strip() == "":
    colours = ["purple", "indigo", "blue", "cyan", "light blue", "white"]
# If the user inputed colours
else:
    custom_colours = custom_colours.strip().split(",")
    colours = custom_colours
# If the user inputed too many colours
    if len(custom_colours) > fractal_settings_dictonary["level_cap"]:
        print("There are too many colours. Using default instead.")
        colours = ["purple", "indigo", "blue", "cyan", "light blue", "white"]
fractal_settings_dictonary["colours"] = colours


# Repeats the pattern 8 times to create a snowflakeish structure
for i in range(8):
    t.color(fractal_settings_dictonary["colours"][i % len(fractal_settings_dictonary["colours"])])
    draw_pattern(int(level), fractal_settings_dictonary["branch_length"])
    t.right(45)
print("There were " + str(fractal_settings_dictonary["call_count"]) + " recursive calls")
turtle.done()
