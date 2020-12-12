import sys

array = {"/": -1, "-": 0, "\\" : 1 ,"(" :  2, "@" : 3,  "?" : 4, ">" : 5, "&" : 6, "%" : 7}

while True :
  n = list(sys.stdin.readline().strip())

  if(n[0] == "#") :
    break
  length = len(n) - 1
  answer = 0
  for i in n :
    answer += array[i] * 8**length
    length -= 1 
  print(answer)
