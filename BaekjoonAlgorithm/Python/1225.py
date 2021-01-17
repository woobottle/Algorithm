a,b = map(list, input().split())

for i in range(len(a)) :
  a[i] = int(a[i])
  
for i in range(len(b)):
  b[i] = int(b[i])

answer = 0
for i in range(len(a)) :
  for j in range(len(b)) :
    answer += a[i] * b[j]
print(answer)
