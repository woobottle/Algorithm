import math
n = input()
l = [0] * 10

for i in n :
  if i == "6" :
    if(l[6] > l[9]) :
      l[9] += 1
    else :
      l[6] += 1
  elif i == "9" : 
    if(l[9] > l[6]):
      l[6] += 1
    else:
      l[9] += 1
  else :  
    l[int(i)] += 1

print(max(l))
