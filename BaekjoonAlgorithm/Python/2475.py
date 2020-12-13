import sys
n = [int(x)**2 for x in sys.stdin.readline().split()]
print(sum(n)%10)
