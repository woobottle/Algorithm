n = int(input())
for i in range(n) :
  l = input()
  a = list(input())
  b = list(input())
  count = 0
  for c in range(len(a)) :
    if(a[c] != b[c]) : count += 1
  print("Case {}:".format(i+1), count)