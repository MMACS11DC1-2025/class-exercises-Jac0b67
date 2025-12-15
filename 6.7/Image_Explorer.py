# Image Explorer project
# Author: jacob Joe
# Date: 11/26/2025

# Goal: Create a program that will analyze satellite imagery and identify man-made structures in the images

import time

t0 = time.time()

from PIL import Image

t1 = time.time()

# This function accepts pixel data and returns an output of true if it matches the definition of
# buildings and false if it doesn't 

def is_target_feature(r, g, b):
    if 80 < r < 130 and 80 < g < 140 and 70 < b < 140:
        return True
    return False

mater_list = []

# Opens image file
images = ["6.7/spot-6-vancouver-canada.jpg", "6.7/Benin-Nigeria.jpg", "6.7/Reese-Michigan.jpg", "6.7/Earth_from_Space_Prague.jpg"]

for i in range(len(images)):
    image_output = Image.open(images[i])
    file = Image.open(images[i])
    sat_image = file.load()

    # Goes through all pixels
    width = file.width
    height = file.height

    # Creates a list to store pixels
    is_target_feature_pixels = []
    water_pixels = []
    green_pixels = []

    # Initialize counter for each colours pixels
    is_target_feature_count = 0
    water_count = 0
    green_count = 0
    
    t2 = time.time()

    # Nested loops will go over pixels from the images and calculate the feature density score for each
    for x in range(width):
        for y in range(height):
            pixel_r = sat_image[x,y][0]
            pixel_g = sat_image[x,y][1]
            pixel_b = sat_image[x,y][2]
            
            # Counts the number of pixels in the target feature
            if is_target_feature(pixel_r, pixel_g, pixel_b):
                is_target_feature_count += 1
                image_output.putpixel((x, y), (241, 9, 38))


    percent_is_target_feature = 100*is_target_feature_count/(width*height)
    report = "The image is {:.2f} percent man-made structures.".format(percent_is_target_feature)
    print(report)

    image_output.save("{}_output.png".format(images[i]))

# Filename and score will be appended to a mater list 
    mater_list.append((images[i], percent_is_target_feature))
# Time module will measure the time it takes to complete the loops

# Outputs the time to three decimal places

# Selection Sort algorithm function will sort the master list based on feature density score from highest to lowest
def sel_sort(mater_list):
    x = len(mater_list)
    for i in range(x):
        largest_index = i

        for j in range(i+1, x):
            if mater_list[j][1] > mater_list[largest_index][1]:
                largest_index = j
        mater_list[i], mater_list[largest_index] = mater_list[largest_index], mater_list[i]
    return mater_list
print(sel_sort(mater_list))
# Binary Search algorithm function will sort through the list for a specific target score