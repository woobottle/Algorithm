import sys 
n = int(sys.stdin.readline().strip())
l = []
for _ in range(n) :
  l.append(sys.stdin.readline().strip())

answer = ""

for i in range(len(l[0])) :
  flag = True
  for j in range(1, n) :
    if(l[0][i] != l[j][i]) : 
      flag = False
      break
  if flag :
    answer += l[0][i]
  else :
    answer += "?"
print(answer)