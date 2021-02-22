def count(number) :
  length_count = 0
  if(number == 0) :
    if(0 not in l) :
      return 1
    else :
      return 1000000
  while(number != 0) :
    c = number % 10
    if(c not in l) :
      length_count += 1
    else : 
      return 100000000
    number //= 10
  return length_count

n = int(input())
m = int(input())
l = [] 
if m != 0 :
  l = list(map(int, input().split()))

answer = n - 100
if(answer < 0) : answer = -answer

for i in range(1000001) :
  length = count(i)
  remain = i - n
  if(remain < 0) : remain = -remain
  if(answer > remain + length) :
    answer = remain + length

print(answer)