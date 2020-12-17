n,m = map(int, input().split())
l = []
for i in range(n) : l.append(i+1)
for k in range(m) : 
  i,j = map(int, input().split())
  temp = l[i-1:j]
  temp.reverse()
  l[i-1:j] = temp

print("".join(str(i) + " " for i in l))

