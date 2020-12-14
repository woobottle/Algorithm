n = int(input())
l = [[0] * 15 for i in range(15)]

for i in range(15) :
  for j in range(15) :
    if(i == 0) :
      l[i][j] = j + 1
    elif(j == 0) :
      l[i][j] = 1
    else :
      l[i][j] = l[i-1][j] + l[i][j-1]

for i in range(n) :
  k = int(input())
  n = int(input())
  print(l[k][n-1])
