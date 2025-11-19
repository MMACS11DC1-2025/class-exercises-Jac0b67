# ReadMe for new_project

# How to use the program:
- The program will prompt the user to input the number of levels they desire to create a snowflake
- It will keep on asking for a valid input until the user provides one between 1 and 9
- After, it will ask the user to input up to 9 colours for the snowflake
- It will automatically genereate with the default colours if the user presses enter or inputs more than 9 colours
- The program will then draw the snowflake and count the number of recursive calls made

# Approach:
- I was trying to create a snowflake fractal art generator that would allow the user
to input the number of levels and customize the colour of the pattern
- I already had the base code for the snowflake fractal so I used that as the starting point
- I wanted to cap the levels at 9 since anything higher would take to long and be inefficent
- I also wanted to increase the levels if the user inputted a number less than or equal to 0
- So I decided to make a while loop that would keep on asking the user for a valid input until they provided one
- I took some inspiration from articles online about how to make recursive fractal art and found some usefull tips about how to keep changing the colour of the pattern
- The number of levels is capped at 9 since I believe it will take the program too long to draw it

# Debugging:
- There were some issues with syntax and more specifically indenting which led the code to not run
- I wasn't able to concatenate certain strings due to me forgetting about not being able to concatenate str and floats
- I had difficulties with the level input since it was not recognizing any input less than or equal to 0 so I changed the input to a float instead of an int


# Testing:
- When I was running it to see how well the while loop was working, I inputted levels 10, 0 and -67 to see if it would handle edge cases
- I was able to see it was able to handle 10 but it did not recognize any user_input equal to or less than 0 so I made level into a float to fix it
- I tried adding in the ability to recognize non-numeric inputs but decided against it as I could not get it to work properly
- It would not recognize any custom colours inputed at first because 

# Test Cases:
- Input: Levels: 5, Colours: red, blue, green, yellow, purple
  - Expected result: A snowflake with 5 levels and the custom colours
  - Actual result: A snowflake with 5 levels and the custom colours
- Input: Levels: 10, 67 , n, Colours: 
  - Expected result: Will keep asking until n is inputed, than outputs snowflake with 6 levels and default colours
  - Actual result: Will keep asking until n is inputed, than outputs snowflake with 6 levels and default colours
- Input: Levels: -3, 0, 4, Colours: blue
  - Expected result: Asks for a valid input until a number between 1 and 9 is given 
  - Actual result: Asks for a valid input until a number between 1 and 9 is given
- Input: Levels: 3, Colours: red, blue, green, yellow, purple, indigo, orange, white, brown,    black
  - Expected result: Will reject custom input and instead go with default colours
  - Actual result: Will reject custom input and instead go with default colours
- Input: Levels: 3, Colours: blahblahblah
  - Expected result: Will use default colours instead  
  - Actual result: Still runs but doesn't print with default colours and instead is just black
  - Difference: I forgot that it would only go with default if the user pressed enter or there were too many colours inputted

# Peer review:
- The fractal offers a lot of freedom(colours, size)
- The code is easy to read
- I like that there is a warning when you put too many levels 
- Code runs without errors