import sys 
n = int(input())

for _ in range(n) :
  r,e,c = map(int, sys.stdin.readline().split(" "))
  if(r < (e-c)) :
    print("advertise")
  elif(r == (e-c)) :
    print("does not matter")
  else :
    print("do not advertise")
