l = list(map(int,input().split()))
[a,b,c] = l
if(a + b + c >= 100) :
  print("OK")
else :
  lindex = l.index(min(l))
  if(lindex == 0) :
    print("Soongsil")
  elif(lindex == 1) :
    print("Korea")
  else :
    print("Hanyang")