l = input()
arr = [0] * 26

for i in list(l) :
  arr[ord(i) - ord('A')] += 1

ans = ''
mid = ''
oddChk = False
for i in range(26) :
  ans += chr(i + ord('A')) * (arr[i] // 2)
  if(arr[i] % 2 == 1) :
    if oddChk : 
      oddChk = -1
      break
    oddChk = True
    mid = chr(i + ord('A'))

if oddChk == -1 :
  print("I'm Sorry Hansoo")
else :
  print(ans + mid + ans[::-1])
