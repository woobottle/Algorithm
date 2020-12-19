l, r, a = map(int, input().split())
total = l + r + a

while a > 0 :
  if(l>r) :
    r += 1
  else :
    l += 1
  a -= 1
print(min(l, r) * 2)