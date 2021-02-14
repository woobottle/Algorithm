def check(arr) :
  for i in range(3) :
    for j in range(3) :
      if(i == 2 and j == 2) : continue
      if(arr[i][j] == ((j+1) + ((i) * 3))) : 
        continue
      else : 
        return False
  return True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

arr = []
for _ in range(3) : 
  arr.append(list(map(int, input().split())))

