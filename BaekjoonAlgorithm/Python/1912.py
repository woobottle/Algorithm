n = int(input())
l = list(map(int, input().split()))

# dp = [[0] * n for i in range(n+1)]
dp = [-9999] * (n+1)
for i in range(len(l)) : 
  if(l[i] < dp[i-1] + l[i]) :
    dp[i] = dp[i-1] + l[i]
  else :
    dp[i] = l[i]


print(max(dp))

