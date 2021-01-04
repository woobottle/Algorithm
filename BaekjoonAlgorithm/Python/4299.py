a,b = map(int, input().split())
n = (a+b)/2
m = a - n
l = [n,m]
l.sort()

if(n%1 != 0 or b >= a) :
  if(b==0 and a ==0) :
    print("0 0")
  else :
    print(-1)
else :
  print("".join(str(int(i)) + " " for i in l[::-1]))