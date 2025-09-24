"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""
print("Welcome to the McDonald how may I take your order?")

print("Welcome to the McDonald how may I take your order?")

burger = input("Would you like a burger for $5? (Yes/No)").lower()
fries = input("Would you like fries for $3? (Yes/No)").lower()

if burger == ("yes") and fries == ("yes"):
    total = int(5) + int(3)
    tax = float(total) * (1.14)
    print("You're total with tax is " + str(tax))
elif burger == ("yes") and fries == ("no"):
    total = int(5) 
    tax = float(total) * (1.14)
    print("You're total with tax is " + str(tax))
elif burger == ("no") and fries == ("yes"):
    total = int(3)
    tax = float(total) * (1.14)
    print("You're total with tax is " + str(tax))
elif burger == ("no") and fries == ("no"):
    total = int(0)
    tax = float(total) * (1.14)
    print("You're total with tax is " + str(tax))