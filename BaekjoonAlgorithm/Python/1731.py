import sys

n = int(sys.stdin.readline())
nrray = [0] * n

for i in range(n) :
  nrray[i] = int(sys.stdin.readline())

if(nrray[n-1] - nrray[n-2] == nrray[n-2] - nrray[n-3]) :
  print(nrray[n-1] + nrray[1] - nrray[0])
else :
  print(int(nrray[n-1] * nrray[1] / nrray[0]))
  