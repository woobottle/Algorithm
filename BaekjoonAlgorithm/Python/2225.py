# 0부터 n까지의 정수 k개를 더해서 그 합이 n이 되는 경우의 수 
# 덧셈의 순서가 바뀐 경우는 다른 경우, 한 개의 수를 여러번 쓸수 있다.
# 다이나믹 
# n,k = map(int, input().split())

# dp = [[0] * (k+1)] * (n+1)

# for i in range(1, n+1) :
#   dp[i][1] = 1

# for i in range(1,k+1) :
#   for j in range(k+1) :
#     for s in range(j+1) :
#       dp[j][i] += dp[s][i-1]

# print(dp[n][k] % 1000000000)


n, k = map(int, input().split())
s = [[0] * 201 for i in range(201)]
for i in range(201):
    s[i][1] = 1
for i in range(1, 201):
    for j in range(201):
        for l in range(j + 1):
            s[j][i] += s[l][i - 1]
print(s[n][k] % 1000000000)
