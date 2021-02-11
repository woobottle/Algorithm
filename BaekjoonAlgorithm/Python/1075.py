n = int(input())
f = int(input())
if(((n//100)*100) % f == 0):
  print("00")
else :
  print(str((((((n//100)*100))//f) + 1) * f)[-2:])
