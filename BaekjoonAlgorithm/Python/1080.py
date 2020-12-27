def change_value(a, b) :
  global l
  for i in range(a, a+3) :
    for j in range(b, b+3) :
      if(l[i][j] == "1") : l[i][j] = "0"
      elif(l[i][j] == "0") : l[i][j] = "1"

def is_same(a,b) :
  for i in range(len(a)) :
    for j in range(len(a[0])) :
      if(a[i][j] != b[i][j]) : return False
  return True


n,m = map(int, input().split())
count = 0

l = []
s = []

for _ in range(n) :
  l.append(list(input()))
for _ in range(n):
  s.append(list(input()))

for i in range(0, n-2) :
  for j in range(0, m-2) :
    if(l[i][j] != s[i][j]) :
      change_value(i,j)
      count += 1

if not (is_same(l,s)) : print(-1)
else : print(count)
