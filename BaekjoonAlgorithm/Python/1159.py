n = int(input())
l = {}

for i in range(n) :
  s = input()[0]
  if s in l :
    l[s] += 1
  else :
    l[s] = 1

answer = ""
for i in sorted(l.keys()) :
  if(l.get(i) >= 5) : answer += i

if answer == "" :
  print("PREDAJA")
else :
  print(answer)