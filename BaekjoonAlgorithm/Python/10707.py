a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

first = a * p
second = 0
if p <= c :
  second = b 
else :
  second = b + (p-c) * d

if(first >= second) : print(second)
else : print(first)

