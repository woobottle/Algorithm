# 그래프로 그려보기, 블로그에 적기
n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1) :
  w, v = map(int, input().split())
  for j in range(0, k+1) :
    if(j < w) :
      dp[i][j] = dp[i-1][j]
      continue
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])
