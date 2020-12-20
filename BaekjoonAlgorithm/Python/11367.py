n = int(input())
for i in range(n) :
  name, point = input().split()
  point = int(point)
  score = "A+"
  if(point <= 59) :
    score = "F"
  elif(point <= 66) :
    score = "D"
  elif(point <= 69):
    score = "D+"
  elif(point <= 76):
    score = "C"
  elif(point <= 79):
    score = "C+"
  elif(point <= 86):
    score = "B"
  elif(point <= 89):
    score = "B+"
  elif(point <= 96):
    score = "A"
  print(name, score)