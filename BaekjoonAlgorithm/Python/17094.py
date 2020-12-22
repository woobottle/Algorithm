n = input()
s = list(input())
ec = s.count("e")
twoc = s.count("2")
if(ec > twoc) :
  print("e")
elif(ec < twoc) :
  print("2")
else :
  print("yee")