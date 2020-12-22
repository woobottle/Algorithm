n = int(input())
l = []
for i in range(n) :
  l.append(int(input()))
if(l[0] == max(l)) :
  print("S")
else :
  print("N")