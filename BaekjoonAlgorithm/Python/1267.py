input()
arr = list(map(int, input().split()))
Y = 0
M = 0
for i in arr :
  Y += ((i//30) + 1) * 10
  M += ((i//60) + 1) * 15

if(Y > M) :
  print("M", M)
elif(Y == M) :
  print("Y", "M", M)
else :
  print("Y", Y)
