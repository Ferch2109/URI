#Turn Left

import fileinput

def position(line):
	arr = ["N","L","S","O"]
	i = 0
	for c in line :
		if c == "E" :
			i -= 1
		if c == "D":
			i +=1
	x = abs(i % 4)
	return arr[x]
	

for line in fileinput.input():
	if line.strip("\n") == "0"	:
		break
	try:
		int(line)
	except:
		print( position(line) )
