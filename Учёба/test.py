sum=0
for n in range(1,10000):
	if n%2==0:
		n//=2
	else:
		n-=1

	if n%3==0:
		n//=3
	else:
		n-=1

	if n%5==0:
		n//=5
	else:
		n-=1
	if n==1:
		sum+=1
print(sum)
