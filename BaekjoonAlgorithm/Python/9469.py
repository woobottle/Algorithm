p = int(input())

for _ in range(p) :
  n,d,a,b,f = map(float, input().split())
  k = (d/(a+b)) * f
  print(n, "%.6f"%(k))