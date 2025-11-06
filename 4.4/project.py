import turtle as tmod  # turtle graphics module

# Settings dictionary: tweak drawing parameters here
settings = {
    "branch_length": 60,  # starting branch length
    "angle": 120,         # angle used between turns
    "colors": ["#c300ff", "#8400ff", "#0004ff", "#0066ff", "#00ccff", "#2fffe3", "#00ffbf57", "white"],
    "max_levels": 9  # safety cap to avoid extreme recursion
}

# Pen and screen will be created when the script runs, not at import time.
screen = None
pen = None

def draw_tree(level, branchLength):
    """
    Recursive snowflake: Draw a branch, then smaller sub-branches.
    Returns the number of recursive calls.
    """
    # base case: stop recursion at level 0 or below
    if level <= 0:
        return 0

    calls = 1  # count this call
    pen.forward(branchLength)  # draw the current branch

    # draw 1st branch
    pen.right(settings["angle"])
    calls += draw_tree(level - 1, branchLength * 0.6)

    # draw 2nd branch
    pen.right(settings["angle"])
    calls += draw_tree(level - 1, branchLength * 0.6)

    # draw 3rd branch 
    pen.right(settings["angle"])
    calls += draw_tree(level - 1, branchLength * 0.6)
    pen.backward(branchLength)  # return to branch base
    
    return calls

def main():
    """Main entry: sets up the turtle, gets user input, draw, and report counts."""
    global pen, screen

    # Set up drawing screen and pen (created at runtime)
    screen = tmod.Screen()
    screen.bgcolor("black")
    pen = tmod.Turtle()

    # Interaction and validation (no try/except)
    levels_custom = input("How many levels do you want to draw? ").strip()
    if levels_custom == "":
        print("No input given. Using 4 levels.")
        levels = 4
    else:
        try:
            levels = int(levels_custom)
            if levels < 0:
                print("Negative level requested. Using 0 instead.")
                levels = 0
            if levels > settings["max_levels"]:
                # fix: convert int to str when concatenating
                print("Requested levels too high. Reducing to " + str(settings["max_levels"]))
                levels = settings["max_levels"]
        except ValueError:
            print("Invalid input. Using max levels.")
            levels = settings["max_levels"]
# 
        
    # Pen initial settings before drawing
    pen.speed(0)
    pen.penup()
    pen.goto(0, 0)
    pen.left(90)   # point upwards
    pen.pendown()
    pen.color("brown")
    pen.width(3)

    # Allow user to override the color palette with a simple comma-separated list.
    # Example input: "#ff0000, #00ff00, blue"
    colors_custom = input("Enter comma-separated colors or just press Enter for default colors: ").strip()
    if colors_custom == "":
        colors = settings["colors"]
    else:
        # user colors and ignore empty entries
        colors = [c.strip() for c in colors_custom.split(",")]
        if len(colors) == 0:
            colors = settings["colors"]
    settings["colors"] = colors

    # Draw multiple trees in a circle, rotating between each one
    total_calls = 0
    for i in range(8):
        pen.pencolor(settings["colors"][i % len(settings["colors"])])
        total_calls += draw_tree(levels, settings["branch_length"])
        pen.right(45)  # rotate before drawing the next tree

    # Report recursion usage and finish
    print("Total recursive calls made: " + str(total_calls))
    tmod.done()

if __name__ == "__main__":
    main()
