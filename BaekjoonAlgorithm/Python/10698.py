n = int(input())
for i in range(n) :
  a,b,c,d,e = input().split()
  answer = ""
  if(b == "+") :
    if((int(a) + int(c)) == int(e)) :
      answer = "YES"
    else :
      answer = "NO"
  else : 
    if((int(a) - int(c)) == int(e)):
      answer = "YES"
    else:
      answer = "NO"
  print("Case %d: %s"%((i+1), answer))