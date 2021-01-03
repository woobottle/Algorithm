l,p = map(int, input().split())
t = list(map(int, input().split()))
s = []

for i in t :
  s.append(i - (l*p))

print("".join(str(i) + " " for i in s))