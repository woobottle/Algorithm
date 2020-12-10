while True :
  n = int(input())
  a = 1
  b = 1

  while a < n :
      b += 1
      a += b

  if b%2 == 0:
      print(str(b-(a-n))+'/'+str(a-n+1))
  else :
      print(str(a-n+1)+'/'+str(b-(a-n)))
