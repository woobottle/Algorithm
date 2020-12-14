import sys

n = [v for v in list(sys.stdin.readline().strip()) if v not in "CAMBRIDGE"]
print("".join([str(l) for l in n]))