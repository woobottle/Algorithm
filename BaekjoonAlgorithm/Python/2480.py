l = sorted(list(map(int, input().split())))
[a,b,c] = l
s = 0
if(l.count(b) == 3) :
  s = int(b) * 1000 + 10000
elif(l.count(b) == 2):
  s = int(b) * 100 + 1000
else : 
  s = int(c) * 100

print(s)