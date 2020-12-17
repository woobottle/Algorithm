t = int(input())

for _ in range(t) :
  n,d = map(int, input().split())
  count = 0
  for i in range(int(n)) :
    v,f,c = map(int, input().split())
    if(v * (f/c) >= d) : count += 1
  print(count)