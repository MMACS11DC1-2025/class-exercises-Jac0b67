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

# This program will open a file containing info from multiple
# students and will determine how many people enjoy the same
# fast_food as you and the person that matches you the least

# Opens a file of student responses
file = open("2.4/responses.csv")
junk = file.readline()

most_relatable = ""
top_score = 0

personal_favourite = file.readline().strip().split(",")

# Goes through every person in the file
for line in file:
    other_favourites = file.readline().strip().split(",")
    if "a&w" in other_favourites():
        
    

for fave in personal_favourites:
    if fave in other_name:
        shared_interest += 1

if shared_interest > top_score:
    most_relatable = other_name
    other_name = shared_interest

print("most_relatable")