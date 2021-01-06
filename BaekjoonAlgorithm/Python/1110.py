n = int(input())

ten = 0
one = 0
if n < 10 :
  one = n
else :
  ten = n // 10
  one = n % 10

count = 0 
target = 0 
if n != 0 :
  while target != n :
    count += 1
    target = int(str(one) + str((one+ten) % 10))
    ten = target // 10
    one = target % 10 
    if(target == n) : break
else :
  count = 1

print(count)
