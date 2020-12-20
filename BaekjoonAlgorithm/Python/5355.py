t = int(input())
for _ in range(t) :
  l = list(input().split())
  answer = float(l[0])
  for i in l[1:] :
    if i == "@" :
      answer *= 3.0
    elif i == "%" :
      answer += 5.0
    elif i == "#" :
      answer -= 7.0
  print("%.2f"%(answer))