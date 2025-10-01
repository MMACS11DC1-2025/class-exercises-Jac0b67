"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# Data Analysis Assignment
# Author: Jacob Joe
# Date: 9/29/2025

# This program will determine how many people in this class enjoy the same 
# kind of fast as you and 
favourite_food = input("Enter your favourite fast food: ").strip().lower()

file = open("2.4/responses.csv")  
header = file.readline()  

lines = file.readlines()


main_data = lines[0].strip().split(",")
main_name = main_data[1]
main_prefs = [item.strip().lower() for item in main_data]

same_food_count = 0
least_relatable = ""
min_shared = float('inf')  

for line in lines:
    data = line.strip().split(",")
    other_name = data[1]
    other_prefs = [item.strip().lower() for item in data]

    shared = 0
    for food in main_prefs:
        if food in other_prefs:
            shared += 1

    if shared < min_shared:  
        min_shared = shared
        least_relatable = other_name

    if favourite_food in other_prefs:
        same_food_count += 1

print("Number of people who like " + str(favourite_food) + " is:" + str(same_food_count))
print("The person the least like you is: " + str(least_relatable))