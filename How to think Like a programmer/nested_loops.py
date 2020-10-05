for outer in range(1,6):
	for inner in range(1,6):
		print(outer,inner)

Strikers = [
			[1,2.4],
            ["Harry Kane","Son","Eriksen"],
            ["Rashford","Martial","Lingard"],
            ["Aguero","Jesus","Sterling"]
           ]
"""for outer in range(0,3):
	for inner in range(0,3):
		print(Strikers[outer][inner])"""

for team in Strikers:
	for player in team:
		print(player)

"""print(Strikers[0][0])
print(Strikers[0][1])
print(Strikers[0][2])
print(Strikers[1][0])
print(Strikers[1][1])
print(Strikers[1][2])
print(Strikers[2][0])
print(Strikers[2][1])
print(Strikers[2][2])"""