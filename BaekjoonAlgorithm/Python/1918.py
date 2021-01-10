# s = list(input().strip())
# stack = []
# letter = []

# for i in range(len(s)) :
#   if(s[i] == "*" or s[i] == "/") :
#     s.insert(i+2, ")")
# print(s)
# for i in s :
#   if(i == "(") :
#     continue
#   elif(i == ")") :
#     while letter :
#       stack.append(letter.pop())
#   elif(i == "+" or i == "-" or i == "*" or i == "/") :
#     letter.append(i)
#   else :
#     stack.append(i)

# while letter :
#   stack.append(letter.pop())

# print("".join(i for i in stack))

priority = {
  '*' : 2,
  '/' : 2,
  '+' : 1,
  '-' : 1,
  '(' : 0
}

stack = []
for c in '(' + input() + ')' :
  if 'A' <= c <= 'Z' :
    print(c, end='')
  elif c == '(' :
    stack.append(c)
  elif c == ')' :
    while True :
      o = stack.pop()
      if o == '(' :
        break
      print(o, end ='')
  else :
    while stack[-1] != '(' and priority[c] <= priority[stack[-1]] :
      print(stack.pop(), end = '')
    stack.append(c)