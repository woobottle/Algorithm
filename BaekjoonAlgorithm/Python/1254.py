s = input()
l = list(s)

ans = 0
head_index = len(s) // 2
tail_index = head_index + 1
if(len(s)%2 == 0) : tail_index = head_index

if(s[:head_index] == s[tail_index:][::-1]): ans = len(s)
else :
  for i in range(1, len(s)) :
    temp = s
    temp += s[:i][::-1]
    head_index = len(temp)//2
    tail_index = head_index + 1
    if(len(temp)%2 == 0) : tail_index = head_index
    if(temp[:head_index] == temp[tail_index:][::-1]): 
      ans = len(temp)
      break
  

print(ans)
