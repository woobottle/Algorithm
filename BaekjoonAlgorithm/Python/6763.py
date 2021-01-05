a = int(input())
b = int(input())
c = b - a
if(c <= 0) :
  print("Congratulations, you are within the speed limit!")
elif(1 <= c and c <= 20) :
  print("You are speeding and your fine is $100.")
elif(21 <= c and c <= 30) :
  print("You are speeding and your fine is $270.")
elif(31 <= c) :
  print("You are speeding and your fine is $500.")
