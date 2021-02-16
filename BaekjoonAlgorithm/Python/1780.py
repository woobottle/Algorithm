import sys

def check(start, end, length) :
  for i in range(start, start+length) :
    for j in range(end, end+length):
      if(arr[start][end] != arr[i][j]) : return False
  return True

def cut(start, end, length) :
  if check(start, end, length) :
    ans[str(arr[start][end])] += 1
  else :
    size = length // 3
    for k in range(3):
      for l in range(3):
        cut(start + size * k, end + size * l, size)

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n) :
  arr.append(list(map(int, sys.stdin.readline().strip().split())))

ans = {"-1":0, "0": 0, "1": 0}

cut(0,0,n)

for _ in list(ans.values()) :
  print(_)
