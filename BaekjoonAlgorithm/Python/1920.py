import bisect 

# def binarySearch(target, start, end) :
#   global nl

#   mid = (start+end) // 2
#   print(start, mid, end)
#   if(start >= end) : return 0

#   if(nl[mid] == target) : return 1
#   elif(nl[mid] > target) :
#     binarySearch(target, start, mid)
#   elif(nl[mid] < target) : 
    # binarySearch(target, mid+1, end)

n = int(input())
nl = set(input().split())
m = int(input())

for i in input().split():
  if i in nl :
    print(1)
  else :
    print(0)
