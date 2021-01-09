import sys 

l = []
for i in sys.stdin.readlines() :
  l.append(int(i))


fl = sorted(l[:4])
sl = sorted(l[4:])
total = sum(fl[1:]) + sum(sl[1:])
print(total)