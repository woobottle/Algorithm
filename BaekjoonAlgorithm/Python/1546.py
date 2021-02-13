n = int(input())
l = list(map(int, input().split()))
max_value = max(l)
total = 0
for i in l :
  total += i/max_value * 100
print(total/n)