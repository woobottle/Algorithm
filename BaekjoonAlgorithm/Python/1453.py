n = int(input())
l = [0] * 101
count = 0
passenger = list(map(int, input().split()))

for i in passenger : 
  if l[i] == 1:
    count += 1
  else :
    l[i] = 1

print(count)