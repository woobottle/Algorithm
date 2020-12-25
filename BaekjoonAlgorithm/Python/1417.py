n = int(input())
l = []
count = 0
for i in range(n) :
  l.append(int(input()))

while True :
  if(max(l) == l[0]) : 
    for j in range(1, len(l)) :
      if(max(l) == l[j]) :
        count +=1 
        break
    break
  l[l.index(max(l))] -= 1
  l[0] += 1
  count += 1

print(count)
