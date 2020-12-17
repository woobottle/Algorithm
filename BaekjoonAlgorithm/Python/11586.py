n = int(input())
l = []
for i in range(n) :
  l.append(input())
t = int(input())

if(t == 1) :
  for i in l :
    print(i)
elif(t == 2) :
  for i in l :
    print(i[::-1])
elif(t == 3) :
  for i in range(n) :
    print(l[n - i - 1])