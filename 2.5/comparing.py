"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# Comparison algorithm
# Author: Jacob Joe 

# 1. Ask the user for their favourite food
# 2. Open the file "responses.csv" and read its contents
# 3. Extract the main user's preferences from the first line of the file
# 4. Initialize variable to count how many student enjoy the same food
# 5. Loop through each line of the file after the first
# 6. Compare the preferences of the user with other students
# 7. Count how many preferences are the same
# 8. If the number of same preferences is greater than the current top score
#    update the most relatable person 
# 9. Count how many students enjoy the same food as the user
# 10. Analyze the comparison operators to make obersvations about preferences
# 11. Print out the results

# Asks for favourite food
favourite_food = input("What is your favourite food? ").strip().lower()

try:
    # Opens file and reads in data
    with open("2.4/responses.csv", 'r') as file:
        header = file.readline()
        lines = file.readlines()
except FileNotFoundError:
    print("Error: Can't find 'responses.csv'.")
    exit()

# Splits first line into main user's data
main_data = lines[0].strip().split(",")
main_name = main_data[1]
main_prefs = [item.strip().lower() for item in main_data[2:]]  # Skip ID and Name

# Initializes variables for counting and comparison
same_food_count = 0
top_score = 0
most_relatable = ""
common_counts = []  # Store how many things in common for each person

# Loops through each line of data after the first
for line in lines[1:]:
    data = line.strip().split(",")
    other_name = data[1]
    other_prefs = [item.strip().lower() for item in data[2:]]  # Skip ID and Name

    things_in_common = 0

    # Count matching preferences
    for fave in main_prefs:
        if fave in other_prefs:
            things_in_common += 1

    common_counts.append(things_in_common)

    # Check for most relatable person
    if things_in_common > top_score:
        most_relatable = other_name
        top_score = things_in_common

    # Count how many people like the same food
    if favourite_food in other_prefs:
        same_food_count += 1

# Comparison operator analysis and observations
total_people = len(lines) - 1
half_prefs = len(main_prefs) // 2
more_than_half = sum(1 for count in common_counts if count > half_prefs)
less_than_half = sum(1 for count in common_counts if count < half_prefs)
exactly_half = sum(1 for count in common_counts if count == half_prefs)

# TESTING: Print out the data used for comparison
# print("DEBUG - main_prefs:", main_prefs)
# print("DEBUG - common_counts:", common_counts)

# Prints out the results
print("Number of people who like " + str(favourite_food) + " is: " + str(same_food_count))
print("The person you would have a good meal with is: " + str(most_relatable))
print(str(more_than_half) + " people share more than half of your preferences.")
print(str(less_than_half) + " people share less than half of your preferences.")
print(str(exactly_half) + " people share exactly half of your preferences.")

    