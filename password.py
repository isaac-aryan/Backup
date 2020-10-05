idb=False
pwb=False

while(idb==False):
	id=input("Enter your valid ID")
	if id.isalnum()==True:
		iwb=True
		break

while(pwb==False):
	password=input("Enter your valid password")
	if password.isdecimal()==True and len(password)<=10:
		pwb=True
		break


