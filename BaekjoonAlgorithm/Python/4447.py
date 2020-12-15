import sys
n = int(input())

for _ in range(n) :
  a = input()
  g_count = a.count("g") + a.count("G")
  b_count = a.count("b") + a.count("B")
  if(g_count > b_count) :
    b = " is GOOD"
  elif(g_count == b_count) :
    b = " is NEUTRAL"
  else :
    b = " is A BADDY"
  print(a + b)

