from collections import Counter

n = int(input())
l = list(map(int, input().split()))
counter = Counter(l)

stack = []
answer = []

if n == 1 :
  print(-1)
else :
  for i in range(len(l) - 1, -1, -1) :
    if stack : 
      if counter[l[i]] > counter[stack[-1]] :
        while stack and counter[stack[-1]] <= counter[l[i]] :
          stack.pop()
        if stack : answer.append(stack[-1])
        else : answer.append(-1)
        stack.append(l[i])
      elif counter[l[i]] == counter[stack[-1]] :
        stack.pop()
        if stack : answer.append(stack[-1])
        else : answer.append(-1)
        stack.append(l[i])
      elif counter[l[i]] < counter[stack[-1]] :
        answer.append(stack[-1])
        stack.append(l[i])
    else :
      stack.append(l[i])
      answer.append(-1)

print(" ".join(str(i) for i in answer[::-1]))