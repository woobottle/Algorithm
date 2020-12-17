l = [1] * 10

  
for i in range(2,10) :
  l[i] =  l[i-1]*i

def calc(i) :
  sum = 0
  if(i == 0) : return 1
  elif(i == 1) : return 2
  elif(i == 2) : return 2.5
  for i in range(0, i+1):
    sum += 1 / l[i]
  return "%.9f"%sum

print("n e")
print("- -----------")
for i in range(0,10) :
  print(i, calc(i))
