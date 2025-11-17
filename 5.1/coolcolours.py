# coolcolours module
# Author: Jacob Joe
# November 14, 2025

def is_green(r, g, b):
    return r >= 0 and r < 130 and g > 150 and g <= 255 and b >= 0 and b < 130: 
    
def colour(r,g,b):    
    if r >= 0 and r < 130 and g > 150 and g <= 255 and b >= 0 and b < 130:
        return "green"
    else:
        return "other"