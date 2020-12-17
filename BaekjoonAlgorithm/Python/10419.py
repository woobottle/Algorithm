n = int(input())
l = [0] * 10001
for i in range(1, 10001) :
  l[i] = i + i**2

for _ in range(n) :
  d = int(input())
  for i in range(10001) :
    if(d < l[i]) : 
      print(i-1)
      break
