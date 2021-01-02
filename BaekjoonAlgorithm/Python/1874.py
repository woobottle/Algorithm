import sys 
n = int(sys.stdin.readline().strip())
l = []
for i in range(n) :
  l.append(int(sys.stdin.readline().strip()))

t = []
answer = []
currNum = 1
flag = True
for i in l :
  while True :
    if flag :
      if t and i == t[-1] : # 끝 원소와 같을때
        answer += ["-"]
        t.pop()
        break
      elif t and i < t[-1] :
        answer.clear()
        flag = False
        break
      else : # 끝 원소와 다를떄
        t.append(currNum)
        answer += ["+"]
        currNum += 1
    else : break

if flag : print(*answer, sep="\n")
else : print("NO")
