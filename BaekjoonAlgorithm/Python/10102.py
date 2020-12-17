n = int(input())
s = list(input())

sa = s.count("A")
sb = s.count("B")

if(sa < sb) :
  print("B")  
elif(sa == sb) :
  print("Tie")
else :
  print("A")
