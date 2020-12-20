n = int(input())

for i in range(n) :
  s = ""
  t = int(input())
  for j in range(1, (t+1)//2) :
    s += str(j) + " " + str(t-j) + ", "
  s = s.rstrip(", ")
  print("Pairs for %.d: %s"%(t, s))