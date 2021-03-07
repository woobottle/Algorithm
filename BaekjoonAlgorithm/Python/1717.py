import sys 
sys.setrecursionlimit(10**6)

def find(num) :
  if(num != arr[num]) :
    # 아래 코드가 경로를 최신화를 매번 해준다
    arr[num] = find(arr[num])
    return arr[num]
  return arr[num]

def union(a, b) :
  A = find(a)
  B = find(b)
  if(A == B) :
    return
  else :
    arr[A] = B

n, m = map(int, sys.stdin.readline().strip().split())

arr = [0] * (n+1)
for i in range(n+1) :
  arr[i] = i

for _ in range(m) :
  status, a, b = map(int, sys.stdin.readline().strip().split())
  if status == 0 :
    union(a,b)
  else :
    if(find(a) == find(b)) :
      print("YES")
    else :
      print("NO")
