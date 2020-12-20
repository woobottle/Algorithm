t = int(input())
for _ in range(t) :
  y = []
  k = []
  for _ in range(9) :
    a,b = map(int, input().split())
    y.append(a)
    k.append(b)
  ys = sum(y)
  ks = sum(k)
  if(ys > ks) :
    print("Yonsei")
  elif (ys == ks) :
    print("Draw")
  else :
    print("Korea")
