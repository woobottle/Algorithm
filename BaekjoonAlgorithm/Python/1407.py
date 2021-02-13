def cal(n) : 
  answer = 0
  i = 1
  while i <= n :
    answer += (i-i//2) * (n//i)
    i *= 2
  return answer

a, b = map(int, input().split())
print(cal(b) - cal(a-1))

