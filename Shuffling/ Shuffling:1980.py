#Shuffling

import fileinput
import math

for line in fileinput.input():
	try:
		int(line.strip())
	except:
		long = len(line.strip())
		f = math.factorial(long)
		print(f)
