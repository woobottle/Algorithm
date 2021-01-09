a,b,c = map(int, input().split())
first = a*b/c
second = a/b*c

if(first >= second) : 
  print(int(first))
else :
  print(int(second))