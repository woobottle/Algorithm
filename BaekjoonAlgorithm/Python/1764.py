# import bisect
# import sys 

# def check(start, target, answer) :
#   for i in start :
#     node = bisect.bisect_left(target, i)
#     if node != len(target) and target[node] == i :
#       answer.append(i)
#   return answer 

# n,m = map(int, sys.stdin.readline().strip().split())
# see = []
# hear = []
# ans = []

# for _ in range(n) :
#   see.append(sys.stdin.readline().strip())
# for _ in range(m) :
#   hear.append(sys.stdin.readline().strip())

# see.sort()
# hear.sort()

# if(n >= m) :
#   ans = check(hear, see, ans)
# else :
#   ans = check(see, hear, ans)

# ans.sort()
# print(len(ans))
# for i in ans :
#   print(i)

import sys 
n, m = map(int, sys.stdin.readline().strip().split())
see = set()
hear = set()

for _ in range(n) :
  see.add(sys.stdin.readline().strip())
for _ in range(m) :
  hear.add(sys.stdin.readline().strip())

ans = list(see & hear)
ans.sort()
print(len(ans))
for i in ans :
  print(i)