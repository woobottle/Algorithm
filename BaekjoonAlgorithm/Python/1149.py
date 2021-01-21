n = int(input())
l = []
dp = [[0] * 3 for _ in range(n+1)]

for _ in range(n) :
  l.append(list(map(int, input().split())))

for i in range(3) :
  dp[0][i] = l[0][i]

for i in range(1, n) :
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + l[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + l[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + l[i][2]

print(min(dp[n-1]))
