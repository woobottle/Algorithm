n = int(input())
l = list(map(int,input().split()))
dp = [[-100000001] * (n) for i in range(n+1)]

for i in range(0,len(l)+1) :
  temp = l[0:]
  if(i != len(l)) :
    temp[i] = 0
  dp[i][0] = temp[0]
  for j in range(1, len(temp)) :
    if(temp[j] < dp[i][j-1] + temp[j]) :
      dp[i][j] = dp[i][j-1] + temp[j]
    else :
      dp[i][j] = temp[j]

print(max(list(map(max,dp))))
