a = input()
b = input()
c = input()

aLen = len(a)
cLen = len(c)
aList = list(a)
cList = list(c)
s = ""

if b == "+" :
  if aLen > cLen :
    aList[aLen - cLen] = "1"
    print("".join(i for i in aList))
  elif aLen < cLen :
    cList[cLen - aLen] = "1"
    print("".join(i for i in cList))
  else :
    s = "2"
    for i in range(aLen - 1) : 
      s += "0"
elif b == "*" :
  s = "1"
  for i in range(aLen + cLen - 2) :
    s += "0"
print(s)
