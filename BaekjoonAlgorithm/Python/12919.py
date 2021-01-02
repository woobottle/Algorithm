s = input()
t = input()
flag = 0


while len(s) != len(t) :
  if t[-1] == "A" :
    t = t[:-1]
  else :
    t = t[::-1]
    t = t[:-1]
  if(t == s) : 
    flag = 1
    break

if flag == 1 :
  print(1)
else : 
  print(0)
