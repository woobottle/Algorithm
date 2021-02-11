start,last = map(int ,input().split())

def calc(num, arr, p) :
  for i in list(str(num)) :
    arr[int(i)] += (1 * p)

arr = [0] * 10
point = 1

while (start <= last) :
  while(start <= last and start % 10 != 0) :
    calc(start, arr, point)
    start += 1
  if(start > last) : break

  while(start <= last and last % 10 != 9) :
    calc(last, arr, point)
    last -= 1
  start //= 10
  last //= 10
  for i in range(10) :
   arr[i] += (last - start + 1) * point 
  point *= 10

ans = 0
for i in range(10) :
  ans += arr[i] * i
print(ans)
