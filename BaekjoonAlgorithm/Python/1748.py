# answer = 0
# divider = 10
# length = 1

# for i in range(1, int(input())+1) :
#   if(i / divider == 1) : 
#     length += 1
#     divider *= 10
#   answer += length

# print(answer)
n = int(input())
ans, i = 0, 1
while i <= n : 
    ans += (n-i+1)
    i *= 10
print(ans)
