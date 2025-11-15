# coolcolours module
# Author: Jacob Joe
# November 14, 2025

def is_green(r, g, b):
    return 0 <= r < 25 and 230 < g <= 255 and 0 <= b < 25
    
def colour(r,g,b):    
    if 0 <= r < 25 and 230 < g <= 255 and 0 <= b < 25:
        return "green"
    else:
        return "other"