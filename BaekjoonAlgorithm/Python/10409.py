import sys 
n,t = map(int, input().split())
l = list(map(int,sys.stdin.readline().strip().split()))
p = []
for i in l :
  if(t >= i) :
    t -= i
    p.append(i)
  else :
    break
print(len(p))
