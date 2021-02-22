n = int(input())

for i in range(1, n+1) :
  s = sorted(list(input()))
  stack = []
  for k in s :
    if stack and stack[-1] == k :
      stack.pop()
    else :
      stack.append(k)
  
  if(stack == []) :
    print("#{}".format(i),"Good")
  else :
    print("#{}".format(i),"".join(stack))
