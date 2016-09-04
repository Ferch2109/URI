#Números sin digitos repetidos

#VERSION 1
"""import fileinput

def valido(n):
	conj = set()
	for c in n:
		conj.add(int(c))
	if len(conj) < len(n):
		return 0
	return 1
	
for line in fileinput.input():
	contador = 0
	param = line.split(' ')
	ini = int(param[0])
	fin = int(param[1])
	for i in range(ini,fin+1):
		contador+=valido(str(i))
	print(contador)"""

#VERSION 2
import fileinput

def valido(n):
	dic = {}
	for c in n:
		if c in dic:
			return 0
		else:
			dic[c] = 1
	return 1

for line in fileinput.input():
	contador = 0
	param = line.split(' ')
	ini = int(param[0])
	fin = int(param[1])
	for i in range(ini,fin+1):
		contador+=valido(str(i))
	print(contador)
