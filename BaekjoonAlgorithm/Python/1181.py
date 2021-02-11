n = int(input())
l = set()
for _ in range(n) :
  l.add(input())
arr = sorted(list(l), key=lambda k: (len(k), k))
ans = ""
print(ans.join(str(i) + "\n" for i in arr))
