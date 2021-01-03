import sys

for i in sys.stdin.readlines() :
  # 소문자, 대문자, 숫자, 공백
  a = 0
  b = 0
  c = 0
  d = 0
  for s in i :
    if s == " " :
      d += 1
    elif ord(s) >= 48 and ord(s) <= 57 :
      c += 1 
    elif ord(s) >= 65 and ord(s) <= 90 :
      b += 1
    elif ord(s) >= 97 and ord(s) <= 122 :
      a += 1  
  print(a,b,c,d)