import sys 
total = 0 
for i in sys.stdin.readlines() :
  if(int(i.rstrip()) < 40) : total += 40
  else : total += int(i)
print(total // 5)