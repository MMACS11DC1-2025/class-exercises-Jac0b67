# Image Explorer project
# Author: jacob Joe
# Date: 11/26/2025

# Goal: Create a program that will analyze satellite imagery and identify man-made structures in the images and give a percentage of the area it takes up

import time

t0 = time.time()

from PIL import Image
Image.MAX_IMAGE_PIXELS = None # Disables limit for the maximum number of pixels
t1 = time.time() # Time up to after image imported

# This function accepts pixel data and returns an output of true if it matches the definition of
# buildings and false if it doesn't 

def is_target_feature(r, g, b):
    if 70 < r < 160 and 70 < g < 160 and 70 < b < 160 or 170 < r < 190 and 100 < g < 150 and 100 < b < 150:
        return "is_target_feature"
    return "other"
    

mater_list = []

# Opens image file
images = ["6.7/spot-6-vancouver-canada.jpg", 
          "6.7/Benin-Nigeria.jpg", 
          "6.7/Reese-Michigan.jpg",
          "6.7/Earth_from_Space_Prague.jpg",
          "6.7/Bourget Airshow, France.jpg",
          "6.7/Manhattan, New-York.jpg",   
          "6.7/Kennedy Space Center.jpg",
          "6.7/Bali, Indonesia.jpg",
          "6.7/Dumont d'Urville Station.jpg",
          "6.7/USS John C. Stennis in Marseille, France.jpg"]

for i in range(len(images)):
    file = Image.open(images[i]).resize((1000, 1000)) # resizes all images to same size for accurate calculations and faster processing
    image_output = file
    sat_image = file.load()

    # Goes through all pixels
    width = file.width
    height = file.height

    # Creates a list to store pixels
    is_target_feature_pixels = []
    

    # Initialize counter for each colours pixels
    is_target_feature_count = 0
    

    # Nested loops will go over pixels from the images and calculate the feature density score for each
    for x in range(width):
        for y in range(height):
            pixel_r = sat_image[x,y][0]
            pixel_g = sat_image[x,y][1]
            pixel_b = sat_image[x,y][2]
            
            # Counts the number of pixels in the target feature
            features = is_target_feature(pixel_r, pixel_g, pixel_b)
            if features == "is_target_feature":
                is_target_feature_count += 1
                image_output.putpixel((x, y), (241, 9, 38))

    percent_is_target_feature = 100*is_target_feature_count/(width*height)
    report = "{} is {:.2f} percent man-made structures.".format(images[i],percent_is_target_feature)
    print(report)

    image_output.save("{}_output.png".format(images[i]))

# Filename and score will be appended to a mater list 
    mater_list.append((images[i], percent_is_target_feature))
# Time module will measure the time it takes to complete the loops
t2 = time.time()
# Outputs the time to three decimal places
module_load = t1-t0
loop = t2-t1
total = t2-t0

timing = "It took {:.3f}s to import PIL and {:.3f}s to loop which is {:.3f}s in total".format(module_load, loop, total)
print(timing)

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

# Output the top 5 results using list slicing
sorted_list = sel_sort(mater_list)
print(sorted_list[:5])

# Binary Search algorithm function will sort through the list for a specific target score
def bin_search(list_of_lists, query):
    search_start_index = 0
    search_end_index = len(list_of_lists)-1

    while search_start_index <= search_end_index:
        midpoint = (search_start_index+search_end_index)//2
        if list_of_lists[midpoint][1] == query:
            return list_of_lists[midpoint][0]
        elif list_of_lists[midpoint][1] < query:
            search_end_index = midpoint - 1
        else:
            search_start_index = midpoint + 1
    return None 
sorted_list = sel_sort(mater_list.copy())

curious = True

# User inputs specific target score of image they want to find
specific_target_score = input("Input the number that represents the is_target_score of the image you want to find from the sorted list or just press enter to stop: ")
# Outputs image name from binary search
if specific_target_score == "":
    print("Hasta la vista, baby")
    curious = False
else:
    specific_target_score = float(specific_target_score)
    print("Here is the image you are looking for: {}".format(bin_search(sorted_list, specific_target_score)))



# While loop so user can keep on searching for images and stop whenever they want
while curious:
    next_search = input("Do you want to search for another image? (Y/N): ").lower()
    if next_search == "y":
        specific_target_score = input("Input the number that represents the is_target_score of the image you want to find from the sorted list: ")
        if specific_target_score != float:
            print("Invalid input. Make sure to input a number like 20.5313")
        else:
            specific_target_score = float(specific_target_score)
            print("Here is the image you are looking for: {}".format(bin_search(sorted_list, specific_target_score)))
    elif next_search == "n":
        print("Don't have a good day, have a great day!")
        curious = False
    else:
        print("Invalid input. Make sure to input Y or N.")