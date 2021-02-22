T = int(input())
for i in range(1,T+1) :
  arr = reversed(list(input()))
  s = []
  for j in arr :
    if(j == "b") :
      s.append("d")
    elif(j == "d") :
      s.append("b")
    elif(j == "p") :
      s.append("q")
    else :
      s.append("p")
  print("#{}".format(i), "".join(s))

