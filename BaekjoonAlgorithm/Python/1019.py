page = int(input())
start = 1
ans = [0] * 10
point = 1

def calc(number, arr, p) :
  for i in str(number) :
    arr[int(i)] += p

while(page >= start) :
  # 끝자리를 9로 맞춰주는 것
  while(page % 10 != 9 and start <= page) :
    calc(page, ans, point)
    page -= 1
  # 끝짜리를 0으로 맞춰주는 것
  while(start % 10 != 0 and start <= page):
    calc(start, ans, point)
    start += 1

  if(page < start) : break

  page //= 10
  start //= 10

  for i in range(10) :
    ans[i] += (page-start+1) * point

  point *= 10

print(*ans)
