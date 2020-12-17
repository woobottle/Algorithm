for _ in range(int(input())) :
  a,b,c,d,e = sorted(map(int, input().split()))
  if(d-b >= 4) :
    print("KIN")
  else :
    print(b+c+d)