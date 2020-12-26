n = list(input())
temp_s = ""
greater_index = -1
answer = ""
for i in range(len(n)) :
  if(n[i] == "<") :
    answer += temp_s[::-1]
    greater_index = i
    temp_s = ""
  elif(n[i] == ">") :
    answer += "".join(i for i in n[greater_index:i+1])
    greater_index = -1
  elif(n[i] == " ") :
    if greater_index == -1 :
      answer += temp_s[::-1]
      temp_s = ""
      answer += " "
  else :
    if greater_index == -1 :
      temp_s += n[i]
    else :
      continue

if(temp_s != "") : answer += temp_s[::-1]
print(answer)
