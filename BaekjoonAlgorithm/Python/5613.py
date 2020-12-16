l = int(input())
while True :
  n = input()
  if(n == "=") : break
  
  p = int(input())
  if n == "+" :
    l += p
  elif n == "-" :
    l -= p
  elif n == "*" :
    l *= p
  elif n == "/" :
    l = int(l // p)

print(l)
