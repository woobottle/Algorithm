import sys 
a,b,c = sorted(map(int, sys.stdin.readline().split()))
s = sys.stdin.readline()

l = ""
for i in s :
  if(i == "A") :
    l += str(a) + " "
  elif(i == "B"):
    l += str(b) + " "
  elif(i == "C"):
    l += str(c) + " "
print(l)
