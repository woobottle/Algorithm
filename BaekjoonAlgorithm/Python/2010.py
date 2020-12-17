import sys

n = int(input())
l = list(map(int, sys.stdin.read().splitlines()))

print(sum(l) - n + 1)