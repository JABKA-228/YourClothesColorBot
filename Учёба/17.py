digits=[]
for i in range(1777, 1800):
    summ=0
    i1=i
    while i !=0:
        summ+=i%10
        i//=10
    if summ%5==0:
        print(i1, summ)
