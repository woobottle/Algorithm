# from itertools import combinations

# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# count = 0
# for i in range(1, n+1) :
#   l = list((combinations(arr, i)))
#   for j in l :
#     if(sum(j) == s) : 
#       count += 1
# print(count)

n, s = map(int, input().split())
x = [0]
for i in map(int, input().split()):
    x += [i+b for b in x]

print(x)
print(x.count(s)-(s == 0))

