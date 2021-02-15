from itertools import combinations, permutations
mo = ['a', 'e', 'i', 'o', 'u']

def check(string) :
  strlen = len(string)
  mo_count = 0
  for i in string :
    if(i in mo) : 
      mo_count += 1
  if((strlen - mo_count) >= 2 and mo_count >= 1) :
    return True
  else :
    return False

l,c = map(int, input().split())
arr = list(input().split())
ans = set()

# 최소 한 개의 모음, 최소 두개의 자음
for i in list(combinations(arr, l)) :
  s = ""
  s = s.join(sorted(list(i)))
  if check(s) :
    ans.add(s)
  
ans = list(ans)
ans.sort()
for i in ans :
  print(i)
