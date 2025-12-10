# ParentBot
# Author: Jacob Joe
# Date: 10/2/2025

score = 0

chores = input("Did you eat? Did you study? Did you do your laundry? Did you call grandma?").lower().strip().split()

completed = 0

for chore in chores:
     if chore in ["yes"]:
        completed += 1

if completed == 0:
    print("I'm coming over.")
elif completed < 3:
    print("Ok.")
elif completed >= 3:
    print("Good!")