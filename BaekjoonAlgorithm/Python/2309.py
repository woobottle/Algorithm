import sys

n = [0] * 9
for i in range(9):
  n[i] = int(sys.stdin.readline())
n.sort()
first_index = 0
second_index = 0

for i in range(9) :
  for j in range(9) :
    if(i >= j) :
      continue
    if(sum(n) - n[i] - n[j] == 100):
      first_index = i
      second_index = j
      break


for i in range(len(n)) :
  if(i == first_index) :
    continue
  elif(i == second_index) :
    continue
  print(n[i])
