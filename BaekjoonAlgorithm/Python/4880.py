import sys 

while True :
  t = sys.stdin.readline().strip()
  if(t == "0 0 0") : break
  a,b,c = map(int, t.split())
  if(b-a == c-b) :
    print("AP " + str(c*2 - b))
  else :
    print("GP " + str(int(c**2 / b)))