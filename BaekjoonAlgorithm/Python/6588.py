length = 1000003
l = [0] * length
l[2] = 1
for i in range(2,int(length**0.5)) :
  for j in range(i*2, length-1, i) :
    if(l[j] == 0) : l[j] = 1

while True :
  n = int(input())
  if(n == 0) : break
  s = "Goldbach's conjecture is wrong."
  for i in range(3,n-1) :
    if(l[i] == 0 and l[n-i] == 0) :
      s = str(n) + " = " + str(i) + " + " + str(n-i)
      break
  print(s)
    
