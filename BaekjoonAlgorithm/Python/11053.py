import bisect
n = int(input())
l = list(map(int, input().split()))
s = [l[0]]

for i in l :
  if(s[-1] < i) :
    s.append(i)
  else :
    s[bisect.bisect_left(s,i)] = i

print(len(s))