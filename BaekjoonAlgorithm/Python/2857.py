import sys

l = []
for i in range(1,6) :
  n = sys.stdin.readline()
  if("FBI" in n) :
    l.append(i)

if len(l) == 0 :
  print("HE GOT AWAY!")
else :
  print("".join(str(i) + " " for i in l))