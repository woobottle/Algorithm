l = [0] * 26
n = int(input())
s = list(input())
for i in range(n) :
  l[i] = int(input())

stack = []
temp = 0 
for i in s :
  if i == "+" :
    first = stack.pop()
    second = stack.pop()
    stack.append(first + second)
  elif i == "-" :
    first = stack.pop()
    second = stack.pop()
    stack.append(second - first)
  elif i == "*" :
    first = stack.pop()
    second = stack.pop()
    stack.append(first * second)
  elif i == "/" :
    first = stack.pop()
    second = stack.pop()
    stack.append(second / first)
  else :
    stack.append(l[ord(i) - 65])

print("%.2f"%stack[-1])
