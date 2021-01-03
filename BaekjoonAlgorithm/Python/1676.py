n = int(input())
two_count = 0
five_count = 0

for i in range(1,n+1) :
  temp = i
  if(temp % 5 == 0) :
    while(temp % 5 == 0 and temp != 0) :
      five_count += 1
      temp /= 5

for i in range(1,n+1) :
  temp = i
  if(temp % 2 == 0 and temp != 0):
    while(temp % 2 == 0):
      two_count += 1
      temp /= 2

if(two_count >= five_count) :
  print(five_count)
else :
  print(two_count)
