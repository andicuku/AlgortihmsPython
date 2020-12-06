import math
import random


def find_square_root(guess, x):
	while (round(guess * guess, 2) != x):
		guess = (guess + (x / guess)) / 2
	return math.trunc(guess)


x = int(input("Enter number to find square root \n"))
guess = random.randrange(1, x)
print(find_square_root(guess, x))
