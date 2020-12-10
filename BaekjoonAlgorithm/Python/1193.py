import sys
a = int(sys.stdin.readline())

n = 1
while True :
  if((n * (n+1)) >= (2 * a)) :
    break
  n += 1

b = (n*(n+1)/2) - a

if(n%2 != 0):
  print(str((b+1)) + '/' + str(n-b))
else :
  print(str((n-b)) + '/' + str(b+1))
  