from itertools import permutations as pr

l = []
for _ in range(9) :
  l.append(int(input()))

for j in list(pr(l,7)) :
  if(sum(j) == 100) : 
    for k in j : print(k)
    break
