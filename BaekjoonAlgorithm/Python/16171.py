s = list(input())
ss = ""
k = input()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in s :
  if(i not in numbers) :
    ss += i

if(k in ss) : print(1)
else : print(0)
