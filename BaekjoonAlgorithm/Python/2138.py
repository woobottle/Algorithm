import sys 
n = int(input())
l = [int(i) for i in list(sys.stdin.readline().strip())]
zero_l = l[:]
non_zero_l = l[:]
s = [int(i) for i in list(sys.stdin.readline().strip())]
  
count = 0

def check_array(i, array):
  global count
  if(array == s): return
  if i == 0 :
    array[i] = (array[i] + 1) % 2
    array[i+1] = (array[i+1] + 1) % 2
    count += 1
  elif i == (len(array) - 1):
    array[i-1] = (array[i-1] + 1) % 2
    array[i] = (array[i] + 1) % 2
    count += 1
  elif(array[i-1] != s[i-1]):
    array[i-1] = (array[i-1] + 1) % 2
    array[i] = (array[i] + 1) % 2
    array[i+1] = (array[i+1] + 1) % 2
    count += 1

for i in range(1, n) :
  check_array(i, non_zero_l)

if(non_zero_l != s) : 
  count = 0
  for i in range(0, len(l)) : check_array(i, zero_l)
  if(zero_l != s) : print(-1)
  else : print(count)
else : print(count)


