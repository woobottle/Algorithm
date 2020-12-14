import sys 

n = int(input())
l = []

for i in range(n) :
  a,b,c,d = sorted(map(int, sys.stdin.readline().split()))
  m = [a,b,c,d]
  e = 0
  if(m.count(d) == 4) :
    e = 50000 + d * 5000
  elif(m.count(c) == 3) :
    e = 10000 + c * 1000
  elif(m.count(d) == 2 and m.count(b) == 2) :
    e = 2000 + d * 500 + b * 500
  elif(m.count(a) == 2 and m.count(b) == 2) : 
    e = 1000 + a * 100
  elif(m.count(b) == 2 and m.count(c) == 2):
    e = 1000 + b * 100
  elif(m.count(c) == 2 and m.count(d) == 2):
    e = 1000 + c * 100
  elif(m.count(b) == 1 and m.count(c) == 1) :
    e = d * 100
  l.append(e)

print(max(l))
