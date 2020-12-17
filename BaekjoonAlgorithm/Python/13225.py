n = int(input())

for i in range(n) : 
  a = int(input())
  count = 0
  for j in range(1, a+1) :
    if(a%j == 0) : count += 1
  print(a, count)