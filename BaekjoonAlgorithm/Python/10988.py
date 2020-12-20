s = list(input())
ss = "".join(i for i in s)

s.reverse()

bs = "".join(i for i in s)
if(ss == bs) :
  print(1)
else :
  print(0)