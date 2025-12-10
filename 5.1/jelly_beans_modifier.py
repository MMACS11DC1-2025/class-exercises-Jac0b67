# Jelly bean image modifier
# Jacob Joe
# November 19, 2025

# This program will go over all pixels in the image, give a percentage for the amount each colour, and replace certain jelly bean colours with white ones

import time

t0 = time.time()

from PIL import Image

t1 = time.time()
# Define a function to return the colour of the pixel
def colour(r,g,b):    
    if r > 150 and g > 150 and b < 10:
        return "yellow"
    elif r > 180 and g < 20 and b < 20:
        return "red"
    elif r > 30 and g > 50 and b < 50:
        return "green"
    elif r > 30 and g > 40 and b < 130:
        return "blue"
    elif r > 90 and g > 40 and b < 180:
        return "purple"

# Opens image file
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

image_output = Image.open("5.1/jelly_beans.jpg")

# Test to see values at 0,0 and what colour() returns
print(jb_image[0,0])
print(colour(jb_image[0,0][0], jb_image[0,0][1], jb_image[0,0][2]))

# Goes through all pixels
width = file.width
height = file.height

# Creates a list to store pixels
yellow_pixels = []
red_pixels = []
green_pixels = []
blue_pixels = []
purple_pixels = []

# Initialize counter for each colours pixels
yellow_pixels_count = 0
red_pixels_count = 0
green_pixels_count = 0
blue_pixels_count = 0
purple_pixels_count = 0

t2 = time.time()

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]
        
        # Adds colours pixels that colours pixel counter
        if pixel_r > 150 and pixel_g > 150 and pixel_b < 100:
            yellow_pixels_count += 1
        elif pixel_r > 180 and pixel_g < 20 and pixel_b < 20:
            red_pixels_count += 1
        elif pixel_r > 30 and pixel_g > 50 and pixel_b < 50:
            green_pixels_count += 1
        elif pixel_r > 30 and pixel_g > 40 and pixel_b < 130:
            blue_pixels_count += 1
        elif pixel_r > 90 and pixel_g > 40 and pixel_b < 180:
            purple_pixels_count += 1

        # Adds colours pixels to list and converts pixel to white 
        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            image_output.putpixel((x, y), (255, 255, 255))
        elif colour(pixel_r, pixel_g, pixel_b) == "red":
            image_output.putpixel((x, y), (255, 255, 255))
        elif colour(pixel_r, pixel_g, pixel_b) == "green":
            image_output.putpixel((x, y), (255, 255, 255))
        elif colour(pixel_r, pixel_g, pixel_b) == "blue":
            image_output.putpixel((x, y), (255, 255, 255))
        elif colour(pixel_r, pixel_g, pixel_b) == "purple":
            image_output.putpixel((x, y), (255, 255, 255))
t3 = time.time()

# Get length of the colours pixel list(same as number of pixels)
# Test how many of that colours pixels counted
print("There are {:.3f} yellow pixels, {:.3f} red pixels, {:.3f} green pixels, {:.3f} blue pixels, {:.3f} purple pixels".format(yellow_pixels_count,red_pixels_count,green_pixels_count,blue_pixels_count,purple_pixels_count))
print(width*height)

# Jellybean report
percent_yellow = 100*yellow_pixels_count/(width*height)
percent_red = 100*red_pixels_count/(width*height)
percent_green = 100*green_pixels_count/(width*height)
percent_blue = 100*blue_pixels_count/(width*height)
percent_purple = 100*purple_pixels_count/(width*height)
report = "There are {:.2f} percent yellow pixels, {:.2f} percent red pixels, {:.2f} percent green pixels, {:.2f} percent blue pixels, {:.2f} percent purple pixels".format(percent_yellow, percent_red, percent_green, percent_blue, percent_purple)
print(report)

# Calculate times
module_load = t1-t0
image_open_load = t2-t1
loop = t3-t2
entire = t3-t0

# Output times
timings = "It took {:.2f}s to import PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all, it took {:.2f}s.".format(module_load, image_open_load, loop, entire)
print(timings)

image_output.save("5.1/jellybean_output.png", "png")