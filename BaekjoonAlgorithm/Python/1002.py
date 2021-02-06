import math
import sys

n = int(sys.stdin.readline().strip())
for _ in range(n) :
  x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
  point_dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  r_dist_max = r1+r2
  r_dist_min = abs(r1-r2)
  if(x1 == x2 and y1 == y2) :
    if(r1 == r2):
      print(-1)
    else :
      print(0)
  else :
    # 내접 혹은 외접
    if(point_dist == r_dist_max or point_dist == r_dist_min) :
      print(1)
    # 내접과 외접 사이
    elif(point_dist < r_dist_max and point_dist > r_dist_min) :
      print(2)
    else :
      print(0)