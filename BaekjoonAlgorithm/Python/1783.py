n,m = map(int, input().split())
answer = 1

if(n == 1) :
  answer = 1
elif(n == 2) :
  answer = min(4, (m+1)//2)
elif(n >= 3 and m <= 6) :
  answer = min(4, m)
elif(n >= 3 and m >= 7) :
  answer = 2 + (m - 4)

print(answer)
