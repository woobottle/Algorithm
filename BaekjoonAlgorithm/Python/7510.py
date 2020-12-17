l = 1
for _ in range(int(input())) :
  a,b,c = sorted(map(int, input().split()))
  print("Scenario #%d:"%l)
  if((c**2 - ((b**2) + (a**2))) == 0) :
    print("yes\n")
  else:
    print("no\n")
  l += 1
