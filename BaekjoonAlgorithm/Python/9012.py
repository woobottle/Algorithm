def checkVps(s) :
  l = []
  for i in s :
    if(i == "(") :
      l.append("(")
    else :
      if(len(l) == 0) :
        return "NO"
      else :
        l.pop()
  if(len(l) == 0) : 
    return "YES"
  else :
    return "NO"

n = int(input())

for i in range(n) :
  s = input()
  print(checkVps(s))