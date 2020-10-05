import time
from datetime import datetime
print(time.time())
#This prints the number of seconds passed since 12 a.m January 1st 1970

print(time.localtime())

print(time.asctime(time.localtime()))

print("Hello")
time.sleep(2)#Sleep function takes the value in seconds
print("Hi, 2 seconds have passed")

print(datetime.now())