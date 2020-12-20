s = int(input())
start = int(s ** 0.5)

while True : 
  if(start*(start+1) <= 2*s and 2*s < start**2 + start*3 + 2) :
    break
  start += 1
print(int(start))