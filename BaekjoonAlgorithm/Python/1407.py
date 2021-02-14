def cal(num) :
  l = bin(num)[2:][::-1]
  a = 1 
  b = 1
  answer = 0
  for i in l :
    if i == '1' :
      answer += a
    a = a * 2 + b
    b *= 2
  return answer

a, b = map(int, input().split())
print(cal(b) - cal(a-1))
