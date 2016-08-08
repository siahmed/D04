#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
def guess_a_number():
	number_guesses = 1
	solution = random.randint(1,25)
	while (number_guesses <= 5):
		number_guesses +=1
		try:
			user_guess = int(input("Guess a number from 1 to 25 "))
		except:
			print("Please make sure to enter a number ")
			continue
		if user_guess > solution:
			print("Too high")
		elif user_guess < solution:
			print("Too low")
		elif user_guess == solution:
			print("Success!")
			break
	else:
		print("-Fin-")

################################################################################
def main():
    
    guess_a_number()

if __name__ == '__main__':
    main()