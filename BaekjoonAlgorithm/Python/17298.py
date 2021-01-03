import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

if n == 1 :
  print(-1)
else :
  for i in range(n-1, -1, -1) :
    if stack :
      if stack[-1] > l[i] :
        answer.append(stack[-1])
        stack.append(l[i])
      elif stack[-1] < l[i] :
        while stack and stack[-1] <= l[i] :
          stack.pop()
        if stack : answer.append(stack[-1])
        else : answer.append(-1)
        stack.append(l[i])
      elif stack[-1] == l[i] :
        stack.pop()
        if stack: answer.append(stack[-1])
        else: answer.append(-1)
        stack.append(l[i])
    else :
      stack.append(l[i])
      answer.append(-1)

  print("".join(str(i) + " " for i in answer[::-1]))
