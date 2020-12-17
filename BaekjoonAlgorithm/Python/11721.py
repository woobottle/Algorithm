n = list(input())

for i in range(0, len(n), 10) :
  print("".join(i for i in n[i:i+10]))
