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

# Interaction and validation (no try/except)
levels_raw = input("How many levels do you want me to draw? ").strip()
if levels_raw == "":
    print("No input given. Using 4 levels.")
    levels = 4
elif levels_raw.lstrip('+-').isdigit():
    levels = int(levels_raw)
    if levels < 0:
        print("Negative level requested; using 0.")
        levels = 0
    if levels > settings["max_levels"]:
        print("Requested levels too high; clamping to " + settings["max_levels"])
        levels = settings["max_levels"]
else:
    print("Invalid input. Using max levels.")
    levels = settings["max_levels"]
    

pen.speed(0)
pen.penup()
pen.goto(0, 0)
pen.left(90)
pen.pendown()
pen.color("brown")
pen.width(3)

# Allow user to override the color palette with a simple comma-separated list.
# Example input: "#ff0000, #00ff00, blue"
colors_raw = input("Enter comma-separated colors (hex codes or names) or press Enter for defaults: ").strip()
if colors_raw == "":
    colors = settings["colors"]
else:
    colors = [c.strip() for c in colors_raw.split(",") if c.strip()]
    if len(colors) == 0:
        colors = settings["colors"]
settings["colors"] = colors

total_calls = 0
for i in range(8):
    pen.pencolor(settings["colors"][i % len(settings["colors"])])
    total_calls += drawTree(levels, settings["branch_length"])
    pen.right(45)




print("Total recursive calls made: " + str(total_calls))
tmod.done()