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
# kind of fast as you and a person you might enjoy eating with

# Asks user for their favourite fast food
favourite_food = input("Enter your favourite fast food: ").strip().lower()

# Opens file
file = open("2.4/responses.csv")  
header = file.readline()  

lines = file.readlines()


main_data = lines[0].strip().split(",")
main_name = main_data[1]
main_prefs = [item.strip().lower() for item in main_data]

same_food_count = 0
top_score = 0
most_relatable = ""
min_shared = float('inf')  

for line in lines:
    data = line.strip().split(",")
    other_name = data[1]
    other_prefs = [item.strip().lower() for item in data]

    things_in_common = 0

    for fave in main_prefs:
        if fave in other_prefs and favourite_food in other_prefs:
            things_in_common += 1

    if things_in_common > top_score:
        most_relatable = other_name
        top_score = things_in_common

    if favourite_food in other_prefs:
        same_food_count += 1

print("Number of people who like " + str(favourite_food) + " is:" + str(same_food_count))
print("The person you would have a good meal with is: " + str(most_relatable))