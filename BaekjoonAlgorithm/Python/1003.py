n = int(input())
l = [[]] * 41
l[0] = [1,0]
l[1] = [0,1]

for i in range(2, 41) :
  l[i] = [x+y for x, y in zip(l[i-2], l[i-1])]

for i in range(n) :
  s = int(input())
  temp = ""
  print(temp.join(str(i) + " " for i in l[s]))
