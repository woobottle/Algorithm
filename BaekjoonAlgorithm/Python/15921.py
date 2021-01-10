n = int(input())
if n == 0 :
  print("divided by zero")
  exit()
l = list(map(int, input().split()))
if(sum(l) == 0) :
  print("divided by zero")
else :
  print("1.00")
