count = 0
for i in range(8) :
  s = input()
  if(i%2 == 0) :
    for j in range(len(s)) :
      if(j%2 == 0 and s[j] == "F") : count += 1
  else :
    for j in range(len(s)) :
      if(j%2 == 1 and s[j] == "F") : count += 1

print(count)