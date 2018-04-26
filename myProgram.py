"""myPython
Simple comment
"""

import random

print(__name__)

def main():
	print("Guess the random number")
	randomNumber = random.randint(1,100)
	found = False
	
	# while not found:
	userGuess = int(input("Your guess: "))
	if userGuess == randomNumber:
		print("Your number is equal")
		found = True
	else:
		print("Guess again")
		main()
	
if __name__ == "__main__":
	main()