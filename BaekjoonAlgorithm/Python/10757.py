a,b = map(list, input().split())
a = a[::-1]
b = b[::-1]
aLen = len(a)
bLen = len(b)
s = ""
d = 0

if aLen > bLen :
  for i in range(bLen) :
    c = int(a[i]) + int(b[i]) + d
    if(c >= 10) :
      d = 1 
      c = str(c-10)
    else : 
      d = 0
      c = str(c)
    s += c
  for i in range(bLen, aLen) :
    c = d + int(a[i])
    d = 0
    s += str(c)
elif aLen < bLen :
  for i in range(aLen):
    c = int(a[i]) + int(b[i]) + d
    if(c >= 10):
      d = 1
      c = str(c-10)
    else:
      d = 0
      c = str(c)
    s += c
  for i in range(aLen, bLen):
    c = d + int(b[i])
    d = 0
    s += str(c)
else :
  for i in range(bLen):
    c = int(a[i]) + int(b[i]) + d
    if(c >= 10):
      d = 1
      c = str(c-10)
    else:
      d = 0
      c = str(c)
    s += c
  if(d == 1):
    s += "1"
  
print(s[::-1])
