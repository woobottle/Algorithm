n = int(input())
cute = 0
ncute = 0
for i in range(n) :
  k = input()
  if(k == "1") :
    cute += 1
  else :
    ncute += 1

if(cute > ncute) :
  print("Junhee is cute!")
else :
  print("Junhee is not cute!")