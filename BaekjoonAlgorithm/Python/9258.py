first = list(input())
second = list(input())

dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(1, len(first)+1) :
  a = first[i-1]
  for j in range(1, len(second)+1) :
    b = second[j-1]
    if(a == b) :
      dp[i][j] = dp[i-1][j-1] + 1
    else :
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp)
print(dp[len(first)][len(second)])