"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""
first = input("Judge 1:")
second = input("Judge 2:")
third = input("Judge 3:")
fourth = input("Judge 4:")
fith = input("Judge 5:")
total = int(first) + int(second) + int(third) + int(fourth) + int(fith)
average = int(total) / int(5)

print("Your Olympic score is " + str(average))

