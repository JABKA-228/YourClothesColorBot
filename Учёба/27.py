f=open("")
s=0
Min=100000
n=int(f.readline())
for i in range(n):
    a=f.readline()
    x=int(a.split()[0])
    y=int(a.split()[1])
    if x>y:
        s+=x
        if x-y<Min: Min=x-y
    else:
        s+=y
        if y-x<Min: Min=y-x
print(s-Min)
