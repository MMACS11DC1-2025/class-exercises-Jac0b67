# Title: Similarity score
# Author: Jacob Joe
# Date: 10/2/2025

print("Please enter your hobbies, separated by spaces.")

person_1 = input("Person 1:").lower().strip().split()
person_2 = input("Person 2:").lower().strip().split()

things_in_common = 0

for person in person_1:
     if person in person_2:
        things_in_common += 1


print("You have " + str(things_in_common) + " hobbies in common")