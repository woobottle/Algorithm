n = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
for i in range(n) :
  a,b = map(int,input().split())
  if(a == 0 or b == 0) :
    axis += 1
  elif(a > 0 and b > 0) :
    q1 += 1
  elif(a > 0 and b < 0) :
    q4 += 1
  elif(a < 0 and b > 0) :
    q2 += 1
  elif(a < 0 and b < 0) :
    q3 += 1

print("Q1: %.f"%q1)
print("Q2: %.f"%q2)
print("Q3: %.f"%q3)
print("Q4: %.f"%q4)
print("AXIS: %.f"%axis)
