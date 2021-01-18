a,b = input().split()

ar = a[::-1]
br = b[::-1]
firstReverse = int(ar) + int(br)
print(int(str(firstReverse)[::-1]))