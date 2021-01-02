s = input()
t = input()
flag = 0

while(len(t) != len(s)) :
  if(t[-1] == "A") :
    t = t[:-1]
  else :
    t = t[:-1]
    t = t[::-1]
  if(s == t) : flag = 1

if flag == 1 :
  print(1)
else :
  print(0)
