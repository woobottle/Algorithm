import sys
t = 0

while True :
  t += 1
  a,b,c = map(int, sys.stdin.readline().strip().split())
  if a == 0 and b == 0 and c == 0 : break
  print("Triangle #{}".format(t))
  if c != -1 and (c <= a or c <= b) :
    print("Impossible.\n")
  elif a == -1 :
    print("a = %.3f" %((c**2-b**2)**0.5), "\n")
  elif b == -1:
    print("b = %.3f" % ((c**2-a**2)**0.5), "\n")
  elif c == -1:
    print("c = %.3f" % ((a**2+b**2)**0.5), "\n")
