w = list(map(int, input().split()))
s = list(map(int, input().split()))

wl = 0
sl = 0
flag = 0

for i in range(9) :
  wl += w[i]
  if(wl > sl) : 
    flag = 1 
    break
  sl += s[i]

if(flag == 1) : print("Yes")
else : print("No")
  
