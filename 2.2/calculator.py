"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
print("Welcome to the happiness calculator! Calculate your happiness and hopefully you will be smiling afterwards.")

score = 0

happy_word = ["happy", "great", "lovely", "awesome", "jolly", "cheerfull"]
neutral_word = ["fine", "alright", "bored", "ok", "good"]
bad_word = ["sad", "horrible", "depressed", "unwell", "down", "miserable", "angry", "mad", "furious", "upset", "annoyed"]

first = input("Input a word that describes how you are feeling today:").lower()
second = input("On a scale of 1-10, how are you feeling overall?").lower()
third = input("Do you feel like you will get better or worse. Yes or No?").lower()

if first in happy_word:
    score += 10
elif first in neutral_word:
    score += 5
elif first in bad_word:
    score += 0
    
if third in ["yes"]:
    score = score * int(second)
    print("Your score is " + str(score))
elif third in ["no"]:
    score = score / int(second)
    print("Your score is " + str(score))
    
if score >= 75:
    print("You're feeling great! Keep it up!")
elif score < 75 and score >= 50:
    print("You're feeling good. Just keep on going with a positive attitude!")
elif score < 50 and score >= 25:
    print("You're probably not feeling great... and that's ok. Just remember that life is like a box of chocolates. You never know what you're gonna get. Maybe tommorow will be a different story.")
elif score < 25:
    print("Stop it, and get some help.")