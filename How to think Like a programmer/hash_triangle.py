
for row in range(1,10):
	if row<=5:	
		for column in range(row):
			print("#",end="")
		print()
	else:
		for column in range(10-row):
			print("#",end="")
		print()
		