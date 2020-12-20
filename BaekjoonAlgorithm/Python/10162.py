n = int(input())
a = 0 
b = 0
c = 0

if(n >= 300) :
  a = n//300
  n %= 300
if(n >= 60) :
  b = n//60
  n %= 60
if(n >= 10):
  c = n//10
  n %= 10


if(n == 0):
  print(a,b,c)
else :
  print(-1)