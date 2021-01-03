s = input()
l = list(s)

stack = []
counter = 0
for i in range(len(l)) :
  if l[i] == "(" :
    stack.append(i)
  else :
    if stack[-1] + 1 == i :
      stack.pop()
      counter += len(stack)
    else :
      stack.pop()
      counter += 1

print(counter)
