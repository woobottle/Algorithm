a = input()
n = int(input())
l = [0] * n
for i in range(n) :
  l[i] = input()

for i in l :
  while True :
    if i in a :
      a = a.replace(i, '')
    else :
      break

if(a == "") :
  print(1)
else :
  print(0)
