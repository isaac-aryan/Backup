height=0
width=0

while(1):
	width=int(input("Please enter the width..."))
	if width<1 or width>100:
		print("Please enter a value in the correct range.")
		continue
	else:
		break
while(1):
	height=int(input("Please enter the height..."))
	if height>=1 and height<=100:
		break
	else:
		print("Please enter a value in the correct range.")
		continue


print("The area of the rectangle is: ",height*width)
print("The perimeter of the rectangle is: ",2*(height+width))


for i in range(width):
	for j in range(height):
		print("*", end="")
	print()

