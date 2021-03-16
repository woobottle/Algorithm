l = [0] * 46
l[1] = 1 
for i in range(2, 46) :
  l[i] = l[i-1] + l[i-2]

n = int(input())

print(l[n])