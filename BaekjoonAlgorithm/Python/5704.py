import sys 

while True :
  n = sys.stdin.readline().strip()
  # if n == "*" : break
  # b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  # flag = 0
  # for i in b :
  #   if(i not in list(n)) :
  #     flag = 1
  #     break
  # if flag == 0 :
  #   print("Y")
  # else :
  #   print("N")
  print(set(n))