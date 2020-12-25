import sys

n = int(input())
l = sorted(list(map(int, sys.stdin.readline().strip().split())))
print(l[(len(l)-1)//2])