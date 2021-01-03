n = int(input())

s = [0] * (n+1)

for i in range(1, n+1) :
  if i == 1000 :
    continue
  elif(i < 100) :
    s[i] = 1
  else :
    temp = list(str(i))
    if((int(temp[2]) - int(temp[1])) == (int(temp[1]) - int(temp[0]))) : s[i] = 1

print(sum(s))