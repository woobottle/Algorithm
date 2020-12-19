n = 123456
nd = ((n * 2) + 1)
l = [1] * (nd + 1)
l[0] = 0
l[1] = 0
s = int(nd**0.5)


for i in range(2,s) : 
  for j in range(i*2, nd+1, i) :
    if(l[j] == 1) : l[j] = 0

while True :
  t = int(input())
  if t == 0 : break
  print(sum(l[t+1:t*2+1]))

