import sys 

l = []
for _ in range(9):
  l.append(int(input()))

for i in range(len(l)-1) :
  for j in range(i+1, len(l)) :
    temp = l[:i] + l[i+1:j] + l[j+1:]
    if(sum(temp) == 100) :  
      for k in sorted(temp) :
        print(k)