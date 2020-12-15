import sys 

e,f,c = map(int, sys.stdin.readline().split())

count = 0
t = e + f
while True : 
  count += t//c
  t = t//c + t%c
  if(t//c == 0) : break

print(int(count))
