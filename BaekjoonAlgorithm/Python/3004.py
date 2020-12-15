n = int(input())

l = [2]
for i in range(1,101) :
  l.append(l[i-1] + ((i+1)//2)+1)

print(int(l[n-1]))