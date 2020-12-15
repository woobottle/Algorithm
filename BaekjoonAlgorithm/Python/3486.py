import sys
n = int(input())

for _ in range(n) :
  a,b = sys.stdin.readline().split()
  c = str(int(a[::-1]) + int(b[::-1]))
  print(int(c[::-1]))    
