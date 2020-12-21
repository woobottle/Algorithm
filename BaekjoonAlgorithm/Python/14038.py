l = []

for i in range(6) :
  l.append(input())

w = l.count("W")
if(w == 5 or w == 6):
  print("1")
elif(w == 3 or w == 4):
  print("2")
elif(w == 1 or w == 2):
  print("3")
else:
  print("-1")
