x = int (input()) 
y = int (input()) 
z=int(input())
n = int (input()) 
ar = [] 
p = 0 
"""for i in range ( x + 1 ) : 
	for j in range( y + 1): 
		if i+j != n: 
			ar.append([]) 
			ar[p] = [ i , j ]
			p+=1 """
ar=[ [ i, j,h] for i in range( x + 1) for j in range( y + 1) for h in range(z+1) if ( ( i + j + h) != n )]
print (ar) 
