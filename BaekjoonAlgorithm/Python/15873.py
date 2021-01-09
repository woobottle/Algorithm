n = input()
a = 0
b = 0
if(len(n) >= 3) :
 a = n[:2]
 b = n[2:]
 if(int(a) > 10) :
   a = n[:1]
   b = n[1:]
else :
  a = n[0]
  b = n[1]

print(int(a) + int(b))