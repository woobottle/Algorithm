t = int(input())
for _ in range(t) :
  n = int(input())
  s = {}
  for i in range(n) :
    a,b = input().split()
    s[a] =  int(b)
  maxValue = max(s.values())
  for key in s.keys() :
    if(s[key] == maxValue) :
      print(key)