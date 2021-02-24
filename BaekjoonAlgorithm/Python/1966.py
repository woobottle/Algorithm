from collections import deque

def check(q, target, array) :
  count = 1
  while True :
    print(q)
    value, index = q.popleft()
    if array[-1] == value :
      array.pop()
      count += 1
    elif(array[-1] == value and target == index) :
      count += 1
      break
    else :
      q.append([value, index])
  return count

test_case = int(input())

for _ in range(test_case) :
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  print(arr)
  l = deque()
  for i in range(len(arr)) :
    l.append([arr[i], i])
  print(check(l, m, arr))