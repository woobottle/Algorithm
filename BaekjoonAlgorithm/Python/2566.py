import sys 

l = []
maxValue = 0
for _ in range(9) :
  l.append(map(int, sys.stdin.readline().split()))

for i in range(9) :
  for j in range(9) :
    if maxValue < l[i][j] :
      maxValue = l[i][j]
      r,c = i, j

# maxValue = max(map(max, l))
print(maxValue)
# newlist = [(i, j) for i in range(9) for j in range(9) if l[i][j] == maxValue]
# print(str(newlist[0][0]+1) + " " + str(newlist[0][1]+1))
print("{} {}".format(r+1, c+1))