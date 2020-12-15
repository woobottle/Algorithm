import sys
t = int(input())

for _ in range(t) :
  p1,p2 = 0,0
  for _ in range(int(input())) :
    s = sys.stdin.readline().strip()
    if s in ["R S", "P R", "S P"] : p1 += 1
    if s in ["S R", "R P", "P S"] : p2 += 1
  if p1 > p2 :
    print("Player 1")
  elif p1 == p2 :
    print("TIE")
  else :
    print("Player 2")