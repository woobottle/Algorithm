import sys 

n = int(input())

for _ in range(n) :
  a = sys.stdin.readline().strip()
  print(a[0].upper() + a[1:])