import turtle

screen = turtle.Screen()
screen.bgcolor("black")
turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.forward(branchLength)
    turtle.left(120)
    drawTree(level-1, branchLength/1.61)
    
    turtle.left(120)
    drawTree(level-1, branchLength/1.61)
    
    turtle.left(120)
    drawTree(level-1, branchLength/1.61)
    turtle.back(branchLength)
    
    
turtle.speed(100)
turtle.penup()
turtle.goto(0, 0)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
levels = input("How many levels do you want me to draw?")

colors = ["#ff0000", "#ff4500", "#ffa500", "#ffd700", "#ffff00", "#adff2f", "#7fff00", "#00ff00"]

for i in range(16):
  turtle.pencolor(colors[i % 8])
  drawTree(int(levels), 60)
  turtle.right(45)
