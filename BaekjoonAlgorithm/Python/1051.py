n,m = map(int, input().split())
arr = []
for i in range(n) :
  arr.append(list(input()))

max_length = min(n, m)  # min(n,m) 은 최대 정사각형의 길이

for i in range(max_length-1, -1, -1):  
  for j in range(0, n-i):  # x 좌표
    for k in range(0, m-i):  # y 좌표
      if(arr[j][k] == arr[j][k+i] == arr[j+i][k] == arr[j+i][k+i]) :
        print((i+1)**2)
        exit()
