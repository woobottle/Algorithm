from collections import deque

n,m = map(int, input().split())
l = deque(map(int, input().split()))
arr = deque()
for _ in range(1, n+1) :
  arr.append(_)

count = 0

while l :
  if(arr[0] == l[0]) : 
    arr.popleft()
    l.popleft()
  else :
    value_index = arr.index(l[0])
    if( len(arr) - value_index > value_index ) : 
      arr.rotate(-value_index)
      count += value_index
    else :
      arr.rotate((len(arr) - value_index))
      count += len(arr) - value_index
    arr.popleft()
    l.popleft()

print(count)
