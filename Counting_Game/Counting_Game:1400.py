#Counting Game

import fileinput

def counting( n, m, k ):
	repeat = 0
	x = 1
	z = 1
	j = 1
	
	while True :
		if x == n and z > 0 :
			x = n
			z = -1
			
		if x == 1 and z < 0:
			x = 1
			z = 1
		
		if x == m :
			if "7" in str(j) or j % 7 == 0 :
				repeat += 1
				if repeat == k:
					return j
		j += 1
		x += z
		#
		if j == 10000 :
			return -1
		

for line in fileinput.input() :
	n,m,k = map( int, line.split(" ") )
	if ( n, m, k ) == ( 0, 0, 0 ) :
		break
	print(counting( n, m, k ) )
