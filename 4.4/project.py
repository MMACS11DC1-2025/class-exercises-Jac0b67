import turtle as tmod

# Settings dictionary
settings = {
    "branch_length": 60,
    "angle": 120,
    "colors": ["#ff0000", "#ff4500", "#ffa500", "#ffd700", "#ffff00", "#adff2f", "#7fff00", "#00ff00"],
    "max_levels": 9  # safety cap to avoid extreme recursion
}

screen = tmod.Screen()
screen.bgcolor("black")
pen = tmod.Turtle()

def drawTree(level, branchLength):
    """
    Simple recursive binary tree: draw a branch, then two smaller sub-branches.
    Returns the number of recursive calls (including this one).
    """
    # base case
    if level <= 0:
        return 0

    calls = 1  # count this call
    pen.forward(branchLength)

    pen.right(settings["angle"])
    calls += drawTree(level - 1, branchLength * 0.6)

    pen.right(settings["angle"])
    calls += drawTree(level - 1, branchLength * 0.6)
    
    pen.right(settings["angle"])
    calls += drawTree(level - 1, branchLength * 0.6)
    pen.backward(branchLength)
    
    return calls

# Interaction and validation
try:
    levels_raw = input("How many levels do you want me to draw? ")
    levels = int(levels_raw)
    if levels < 0:
        raise ValueError("levels must be non-negative")
    if levels > settings["max_levels"]:
        print("Requested levels too high; clamping to " + settings[float('max_levels')])
        levels = settings["max_levels"]
except ValueError:
    levels = 9
    print("Extreme recursion detected. Using max level instead.")
    

pen.speed(0)
pen.penup()
pen.goto(0, 0)
pen.left(90)
pen.pendown()
pen.color("brown")
pen.width(3)

total_calls = 0
for i in range(16):
    pen.pencolor(settings["colors"][i % len(settings["colors"])])
    total_calls += drawTree(levels, settings["branch_length"])
    pen.right(45)

print("Total recursive calls made: " + str(total_calls))
tmod.done()