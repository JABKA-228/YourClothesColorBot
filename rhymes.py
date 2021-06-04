import random


listofwords = []
a = []
with open('russian.txt') as inf:
    for line in inf:
        line = line.strip()
        a.append(line)

rhymes = []

z = 0
l = 0

random.shuffle(a)

word = input()
for i in range(len(a)):
    l = a[i]
    if l[-2:] == word[-2:] and z < 3:
        z += 1
        rhymes.append(l)
print(*rhymes)
