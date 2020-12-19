# 입력을 받고 그 수에 해당하는 부분까지만 아래 for문을 돌려도 되었을것 같다
maxNum =1000000
l = [0] * maxNum
l[0] = 1
l[1] = 1

for i in range(2, int(maxNum ** 0.5)):
  for j in range(i*2, maxNum, i):
    if(l[j] == 0):
      l[j] = 1

m,n = map(int, input().split())

s = []
for i in range(m, n+1) :
  if(l[i] == 0) :
    s.append(i)

for i in s :
  print(i)