'''with open("24.txt","r") as file:
	s=file.readline()

'''
'''
for n in range(400000000, 600000001):
	spisok=[]
	for m in range(2, 10000000, 2):
		for n in range(1, 1000000, 2):
'''
s = 14
for i in range(10000):
	x=i
	s = 100*s + x
	n = 1
	while s < 2021:
	  s = s + 5*n
	  n = n + 1
	if n==17:
		print(i)
		