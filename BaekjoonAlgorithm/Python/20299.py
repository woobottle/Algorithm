import sys
n, k, l = map(int, input().split())
s = ""
count = 0
for i in range(n) : 
  a,b,c = map(int, sys.stdin.readline().strip().split())
  if((a + b + c) >= k and a >= l and b >= l and c >= l) :
    s += str(a) + " " + str(b) + " " + str(c) + " "
    count += 1

print(count)
print(s)

