import bisect
n = int(input())
l = []
for i in range(1, 1000001) :
  temp = str(i).replace("7", "")
  temp = temp.replace("4", "")
  if(temp == "") : l.append(i)
print(l[bisect.bisect(l,n) - 1])