n = int(input())
s = sorted(list(map(int, input().split())))
print(s[0] * s[-1])