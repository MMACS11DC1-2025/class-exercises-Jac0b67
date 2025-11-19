# coolcolours module
# Author: Jacob Joe
# November 14, 2025

from PIL import Image
import coolcolours

def is_green(r, g, b):
    if 0 <= r < 25 and g > 150 and 0 <= b < 120:
        return True
    else:
        return False

# Opens image files A (green) and B (background)
image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

# Makes a output canvas C to draw 
image_output = Image.open("5.1/kid-green.jpg")

# Find the widths and heights of the images
width = image_output.width
height = image_output.height

# Goes through all pixels in A
for i in range(width):
    for j in range(height):
        r = image_green[i, j][0]
        g = image_green[i, j][1]
        b = image_green[i, j][2]

        # Replace green pixel with B value
        if coolcolours.is_green(r,g,b):
            beach_colour = image_beach[i,j] 
            image_output.putpixel((i,j), beach_colour)
image_output.save("5.1/output.png", "png")
