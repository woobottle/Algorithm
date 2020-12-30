l = input()
s = ""
answer = 0
temp = 0
flag = 0

for i in l :
  if(i == "+" and flag == 0) :
    answer += int(s)
    s = ""
  elif(i == "+" and flag == 1) :
    temp += int(s)
    s = ""
  elif(i == "-" and flag == 0) :
    answer += int(s)
    flag = 1
    s = ""
  elif(i == "-" and flag == 1):
    temp += int(s)
    s = ""
  else :
    s += i

if(flag == 0) : answer += int(s)
else : temp += int(s)

print(answer - temp)
