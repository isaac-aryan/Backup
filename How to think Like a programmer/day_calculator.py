month=int(input("Enter the month..."))
day=int(input("Enter the day..."))

year=[31,28,31,30,31,30,31,31,30,31,30,31]


current=year[0:month-1]

total=sum(current)+day

print("The total days are ",total)