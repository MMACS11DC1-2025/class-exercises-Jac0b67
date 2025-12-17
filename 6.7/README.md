# README for Image Explorer

# Project Overview:
- This project will create a program that will be able to scan multiple images of satellite imagery and identify buildings and structures
- It should be able to identify buildings, roads, bridges and most man-made structures.
- From above, these features heavily contrast from natural and vegetated aras as they have very different colours
- This should make it easy for the program to clearly distinct structures from its surrondings


# Feature Detection and Justification
- Main goal is to identify most man-made structure ie builings, roads, bridges
- The colours of man-made structures, vegetation and other features have a very different colour
range which should make it easier to distinguish man-made structures from the rest
- Identifying water, vegetation, clouds and other natural features was an optional goal
but proved too difficult and complicated to implement consistently and effectively due
to the different lighting conditions and colour pallete in each image
- Most structures were grey so I went with "70 < r < 160 and 70 < g < 160 and 70 < b < 160" to identify
light grey pixels, the most common colour of concrete and steel strcutures
- However many other structures were brighter and more brown or red in colour from being made of brick such as the roofs of some buildings in Marseille, so I had to also include those colours "or 170 < r < 190 and 100 < g < 150 and 100 < b < 150" for is_target_feature
- Should be able to identify a majority of structures and give a sense of how much of the area has been developed and used


# Testing and Validation
- Started testing with only a few images to analyze to give quicker feedback and simplify things
- Repeatedly tested and optimized is_target_feature until it gave optimal results
- Provided simple test cases for each functions

- Test for Selection Sort Algorithm(Commit version 3):
    Input: print(sel_sort(mater_list))
    Expected Output: Sorted Mater List by highest to lowest density score
    Actual Output: Sorted Mater List by highest to lowest density score

- Test for Binary Search Algorithm(Commit version 3):
    Input: print(bin_search(mater_list, 5))
    Expected Output: Reese Michigan
    Actual Output: Reese Michigan

- Test for Binary Search Algorithm(Commit version 5):
    Input: 14.1928
    Input 2: Y
    Input 3: 28.8751
    Input 4: N

    Expected Output: Here is the image you are looking for: 6.7/spot-6-vancouver-canada.jpg
    Expected Output 2: Do you want to search for another image? (Y/N):
    Expected Output 3: Here is the image you are looking for: 6.7/Bourget Airshow, France.jpg
    Expected Output 4: Do you want to search for another image? (Y/N):
    Expected Output 5: Have a nice day!:

    Actual Output: Here is the image you are looking for: 6.7/spot-6-vancouver-canada.jpg
    Actual Output 2: Do you want to search for another image? (Y/N):
    Actual Output 3: Here is the image you are looking for: 6.7/Bourget Airshow, France.jpg
    Actual Output 4: Do you want to search for another image? (Y/N):
    Actual Output 5: Have a nice day!:

- Test for Binary Search Algorithm(Commit version 5):
    Input: 

    Expected Output: -1

    Actual Output: ValueError: could not convert string to float: ''

- Test for Binary Search Algorithm(Commit version 6):
    Input: 

    Expected Output: Hasta la vista, baby

    Actual Output: Hasta la vista, baby

- Test for Binary Search Algorithm(Commit version 6):
    Input: 20.5313
    Input 2: fdhgfufh
    Input 3: Y
    Input 4: kfgjdsgfhs
    Input 5: N

    Expected Output: 6.7/Earth_from_Space_Prague.jpg
    Expected Output 2: Do you want to search for another image? (Y/N):
    Expected Output 3: Invalid input. Make sure to input Y or N.
    Expected Output 4: Do you want to search for another image? (Y/N):
    Expected Output 5: Input the number that represents the is_target_score of the image you want to find from the sorted list:
    Expected Output 6: Invalid input. Make sure to input a number like 20.5313
    Expected Output 7: Do you want to search for another image? (Y/N):
    Expected Output 8: Don't have a good day, have a great day!

    Actual Output: 6.7/Earth_from_Space_Prague.jpg
    Actual Output 2: Do you want to search for another image? (Y/N):
    Actual Output 3: Invalid input. Make sure to input Y or N.
    Actual Output 4: Do you want to search for another image? (Y/N):
    Actual Output 5: Input the number that represents the is_target_score of the image you want to find from the sorted list:
    Actual Output 6: Invalid input. Make sure to input a number like 20.5313
    Actual Output 7: Do you want to search for another image? (Y/N):
    Actual Output 8: Don't have a good day, have a great day!


# Performance analysis/Code Profiling
- Noticed slow preformance from the start after importing multiple images
- Likely due to the nested loops, since the number of operations grows quadratically O(n^2)
- Some images were too large and could not import due to size limit
- Resized images to 1000 by 1000 to optimize preformance and reduce the time needed
- Used time module to calculate the time taken to process the images
- Had to add "Image.MAX_IMAGE_PIXELS = None" line so hat I would be able to import some
of the larger images
- Outputed time as a human-readable report that displays the time it takes to import the image,
complete the nested loop, and the total time to three decimal places.


# Challenges faced
 - I took some time to wonder about what my program would do and kept on slightly changing the goals until I settled on finding the percentage
 of man-made structures in the images since I thought it would be easy to identify the objects from its surrondings
 - Trying to find suitable images and information for project that meet the criteria and goals
 - Optimization was a major challenge since most images were too large and it took some time to
 find a solution to change the size of the images and remove the limit on the number of pixels allowed in the images
 - Optimizing the is_target_feature function was the biggest challenge since I had to find a way to make it work as intended for all the images I used and a lot of the images had different lighting, colours, and unique features that made it challenging to create a solution that works for all of them


 # Real world applications
 - There are many usefull aplications for identifying land development as it can show underlying trends and how they play out
 - It reveals how we are shaping the world and how it impacts the local environment 
 - Data is usefull in planning sustainable development and might reveal any unforseen risks and consequences
 - Many organizations, both government and private, heavily analyize land-use cover
 