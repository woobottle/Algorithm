# def binary_select(array, start, last, target) : 
#   half_index = len(array) // 2
#   if(array[half_index] == target or start == last) : return half_index
#   elif(array[half_index] < target) :
#     start = half_index
#     binary_select(array[0:half_index], start, last, target)
#   else :
#     last = half_index
#     binary_select(array[half_index:-1], start, last, target)

def binary_select(array, target) :
  l,h = 1,len(array)-1
  while l<h:
    m = (l+h)//2
    if(s[m] < target) :
      l = m+1
    elif(s[m] > target) :
      h = m
    else :
      l = h = m
  return h


n = int(input())
l = list(map(int, input().split()))
s = [l[0]]
start = 0
last = len(l) - 1
for i in l :
  if s[-1] < i :
    s.append(i)
  else :
    s[binary_select(s, i)] = i
print(len(s))
