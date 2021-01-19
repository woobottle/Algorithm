n = int(input())
l = []

for _ in range(n) :
  l.append(list(map(int, input().split())))
answer = 999999999
dp = [[0] * 3 for _ in range(n+1)]

for j in range(3) :
  for i in range(3) :
    if(i == j) :
      dp[0][i] = l[0][i]
    else :
      dp[0][i] = 9999999
  for i in range(1,n) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + l[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + l[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + l[i][2]
  for i in range(3) :
    if(i == j) : continue
    answer = min(answer, dp[n-1][i])
    

print(answer)