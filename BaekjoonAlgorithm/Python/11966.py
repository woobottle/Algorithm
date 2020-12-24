a = int(input())


while True :
  if(a == 1 or a == 2) : 
    print("1")
    break
  elif(a < 2) :
    print("0")
    break
  a /= 2
