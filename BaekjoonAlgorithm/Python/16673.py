c, k, p = map(int, input().split())
s = 0
for i in range(1,c+1) :
  s += ((i * k) + (i*i*p))
print(s)