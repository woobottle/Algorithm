n = int(input())
dp = [0] * 100001
dp[1] = 1

for i in range(1, n+1) :
  dp[i] = i
  tempIndex = int(i**0.5)
  for j in range(1,tempIndex+1) :
    if(dp[i] > dp[i - j*j] + 1) :
      dp[i] = dp[i-j*j] + 1
    
print(dp[n])
