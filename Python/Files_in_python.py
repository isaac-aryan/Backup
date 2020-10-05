My_file=open("Football.txt","r+")
print("Name of the file: ",My_file.name)
print("Closed or not: ",My_file.closed)
print("Opening Mode: ",My_file.mode)
#My_file.write("I support Tottenham Hotspur FC")
print(My_file.read(10))

My_file.close()

import os
os.rename("Football.txt","My Club.txt")