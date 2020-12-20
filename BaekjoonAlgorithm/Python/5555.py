s = input()
n = int(input())
count = 0 

for _ in range(n) :
  c = input()
  c = c + c
  if(s in c):
    count += 1


print(count)