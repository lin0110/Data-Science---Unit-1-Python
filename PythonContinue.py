#Your task here is very special: you must design a vowel eater! Write a program that uses:
#A for loop	
#The concept of a conditional execution (if-elif-else)
#The continue statement
#use conditional execution and the continue statement to "eat" the following vowels: 
#              A, E, I, O, U from the inputted word
#print the uneaten letters to the screen, each one of them on a separate line

# Prompt the user to enter a word and assign it to the userWord variable.
userWord = input("Enter a word ") 

for letter in userWord:
    #Complete the body of the for loop.
    #Create a series of if-elif statements with the continue argument
    
    if letter.upper() == "A":
      continue
    elif letter.upper() == "E":
      continue
    elif letter.upper() == "I":
      continue
    elif letter.upper() == "O":
      continue
    elif letter.upper() == "U":
      continue


    #print out the remaining letters
    print(letter)
