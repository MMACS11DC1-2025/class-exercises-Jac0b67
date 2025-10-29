import turtle

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.forward(branchLength)
    turtle.left(40)
    drawTree(level-1, branchLength/1.61)
    
    turtle.right(80)
    drawTree(level-1, branchLength/1.61)
    
    turtle.left(40)
    turtle.back(branchLength)
    
    
turtle.speed(0)
turtle.penup()
turtle.goto(0, -100)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
levels = input("How many levels do you want me to draw?")
for i in range(8):
  drawTree(int(levels), 60)
  turtle.right(45)
