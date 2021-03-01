n = int(input())
x,y = 0, 0
horizontal = [[False] * n for _ in range(n)]
vertical = [[False] * n for _ in range(n)]

for c in input() :
  if c == "R" :
    if y == n-1 : continue
    horizontal[x][y] = True; y+=1; horizontal[x][y] = True
  if c == "L" :
    if y == 0 : continue
    horizontal[x][y] = True; y-=1; horizontal[x][y] = True
  if c == "D" :
    if x == n-1 : continue
    vertical[x][y] = True; x+=1; vertical[x][y] = True
  if c == "U" :
    if x == 0 : continue
    vertical[x][y] = True; x-=1; vertical[x][y] = True

for x in range(n) :
  for y in range(n) :
    if(horizontal[x][y] and vertical[x][y]) : print("+", end = "")
    elif(horizontal[x][y]) : print("-", end = "")
    elif(vertical[x][y]) : print("|", end = "")
    else : print(".", end = "")
  print()
