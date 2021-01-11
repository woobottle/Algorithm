d = [0] * 1000001
d[0] = 0
d[1] = 0
d[2] = 1

n = int(input())

for i in range(3,n+1) : 
  if(i % 6 == 0) :
    d[i] = min(min(d[i//2] + 1, d[i//3] + 1), d[i-1] + 1)
  elif(i % 3 == 0) :
    d[i] = min(d[i//3] + 1, d[i-1] + 1)
  elif(i % 2 == 0) :
    d[i] = min(d[i//2] + 1, d[i-1] + 1)
  else : 
    d[i] = d[i-1] + 1

print(d[n])
