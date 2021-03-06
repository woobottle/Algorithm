n,m = map(int, input().split())

set_list = {}
for i in range(n+1) :
  set_list[i] = set([i])

for _ in range(m) :
  status, a, b = map(int, input().split())
  if status == 0 :
    set_list[a] = set_list[a] | set_list[b]
    set_list[b] = set_list[a] | set_list[b]
  else :
    if b in set_list[a] : 
      print("YES")
    else : 
      print("NO")