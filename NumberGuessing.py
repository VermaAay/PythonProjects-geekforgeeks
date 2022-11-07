import random
import math

# Taking Inputs

lower = int(input("Enter lower bound :- "))

upper = int(input("Enter upper bound :- "))

#generating a random number between upper and lower bounds

x = random.randint(lower,upper)
print("\n\t You have only got", round(math.log(upper-lower + 1,2)), "chances to guess the number!\n")

#intitializing number of guesses

count = 0

# for calculation of minimum no of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1
	guess = int(input("Guess a number:- "))

	#Conditions testing
	if x==guess:
		print("Congratulations you did it in ",count ," try")
		#Once guessed correctly loop will break
		break
	elif x > guess:
		print("Aww! You guessed too high ! Try Again !")
	elif x < guess:
		print("Aww ! You guessed too low ! Try again !")

	#If guessing is more than the required amount of guesses then

	if count >= math.log(upper-lower + 1,2):
		print("\n The number is %d\n" % x )
		print("Better Luck Next Time")