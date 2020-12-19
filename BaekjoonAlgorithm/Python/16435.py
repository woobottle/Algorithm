n, k = map(int, input().split())
l = sorted(list(map(int, input().split())))

for i in l :
  if(k >= i) : k += 1
  else : break

print(k)
