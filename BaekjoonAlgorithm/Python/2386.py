import sys 

while True :
  n = [x.lower() for x in list(sys.stdin.readline().strip())]
  target = n.pop(0)
  if target == "#" :
    break
  count = 0
  for i in n :
    if i == target :
      count += 1
  print(target + " " + str(count))
