x, y, c = map(float, input().split())

def get_num(k) :
  h1 = (x**2 - k**2)**0.5
  h2 = (y**2 - k**2)**0.5
  return (h1 * h2) / (h1 + h2)

left = 0.0
right = min(x,y)

while(right - left > 0.0001) :
  mid = (left + right) / 2
  if(get_num(mid) >= c) :
    left = mid
  else :
    right = mid

print(format(left, ".3f"))