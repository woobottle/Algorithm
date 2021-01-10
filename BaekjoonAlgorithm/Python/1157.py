l = list(input().upper())
s = set(l)
d = {}

for i in s :
  d[i] = l.count(i)

maxValue = max(d.values())
answer = ""
for i in d.keys() :
  if(answer == "" and d[i] == maxValue) : answer = i
  elif(answer != "" and d[i] == maxValue) : 
    answer = "?" 
    break

print(answer)