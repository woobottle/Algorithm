case = 1
answer = 0
while True :
  l, p, v = map(int, input().split())
  if(l == 0 and p == 0 and v == 0) : break

  div, mod = divmod(v,p)
  answer = l * div
  if(mod <= l) :
    answer += mod
  else :
    answer += l

  print("Case ", case, ": ", answer, sep = "")
  case += 1