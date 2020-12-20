i = 1
while True :
  n = int(input())
  if(n == 0) : break
  if(n % 2 == 0) :
    print("%.d. even %.d"%(i, n//2))
  else :
    print("%.d. odd %.d" % (i, (n-1)//2))
  i += 1
