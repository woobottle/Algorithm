l = [] 
for i in range(28) : 
  l.append(int(input()))
l.sort()

j = [i for i in range(1,31)]

for i in range(28) :
  j.pop(j.index(l[i]))

for i in j : print(i)