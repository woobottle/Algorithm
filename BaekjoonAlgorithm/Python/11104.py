n = int(input())
for _ in range(n) :
  answer = 0
  s = list(input())
  for i in range(24) :
    if(s[i] == "1") :
      answer += 2**(23-i)
  print(answer)