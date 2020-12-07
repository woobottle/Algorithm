# def checkArray(array):
#   arrayLength = len(array) - 1 
#   stringArray = [*array]
#   for num in range(len(array)):
#     if(stringArray[num] != stringArray[arrayLength-num]):
#       print("no")
#       return
      
#   print("yes")
  

# while True :
#   num = input()
#   if num == "0" :
#     break
  # checkArray(str(num))

import sys 
  
while True :
  num = sys.stdin.readline().strip()
  if num == "0" : break
  print('yes' if num==num[::-1] else 'no' )