def odd_number(n) :
  l = [0] * n
  a = int(n ** 0.5)
  for i in range(2, a+1) :
    if l[i] == 0 :
      for j in range(i*2, n, i) :
        l[j] = 1
  return [i for i in range(2,n) if l[i] == 0]

array = odd_number(1000)

n = int(input())
a = list(map(int,input().split()))
l_count = 0

for i in a :
  if(i in array) :
    l_count += 1
print(l_count) 
 
