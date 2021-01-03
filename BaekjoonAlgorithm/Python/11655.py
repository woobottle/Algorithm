s = input()
answer = ""
for i in s :
  if(i == " ") :
    answer += " "
  else :
    if(ord(i) >= 65 and ord(i) <= 90) :
      if(ord(i) + 13 > 90) :
        answer += chr(65 + ord(i) + 13 - 91)
      else :  
        answer += chr(ord(i) + 13)
    elif(ord(i) >= 97 and ord(i) <= 122):
      if(ord(i) + 13 > 122):
        answer += chr(97 + ord(i) + 13 - 123)
      else:
        answer += chr(ord(i) + 13)
    else :
      answer += i
print(answer)
