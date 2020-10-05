import random as r
num=r.randint(1,10)
guess=0
tries=0

while guess!=num and tries<=5:
	guess=int(input("Enter the number between 1 and 10."))
	if guess<num:
		print("Try again. Your guess is too low.")
	elif guess>num:
		print("Try again. Your guess is too high.")
	else:
		print("Congratulations! You took ",tries," tries to guess the number.")
		break
	tries+=1
	print("Tries left: ",5-tries)

if tries>5:
	print("Oops! You lost. You have no tries left.")