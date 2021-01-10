br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

bCount = 0
dCount = 0

bx = abs(jr-br)
by = abs(jc-bc)

while True :
  if(bx == 0 and by == 0) : break
  elif(bx - 1 >= 0 and by - 1 >= 0) : 
    bCount += 1 
    bx -= 1
    by -= 1
  elif(bx == 0 and by - 1 >= 0) :
    bCount += 1
    by -= 1
  elif(bx - 1 >= 0 and by == 0) :
    bCount += 1
    bx -= 1

dCount = abs(jr-dr) + abs(jc-dc)


if bCount < dCount :
  print("bessie")
elif bCount == dCount :
  print("tie")
else :
  print("daisy")
