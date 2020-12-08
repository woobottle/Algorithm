n = int(input())

nArray = [-1] * 5001
nArray[3] = 1; nArray[5] = 1; nArray[6] = 2; nArray[8] = 2; nArray[9] = 3; nArray[10] = 2;

for i in range(11,5001) : 
  if(nArray[i-3] == -1 & nArray[i-5] == -1) :
    continue
  elif(nArray[i-3] == -1 & nArray[i-5] != -1) :
    nArray[i] = nArray[i-5] + 1
  elif(nArray[i-3] != -1 & nArray[i-5] == -1) :
    nArray[i] = nArray[i-3] + 1
  elif(nArray[i-3] != -1 & nArray[i-5] != -1) :
    if(nArray[i-3] > nArray[i-5]):
      nArray[i] = nArray[i-5] + 1
    elif(nArray[i-5] > nArray[i-3]):
      nArray[i] = nArray[i-3] + 1
    elif(nArray[i-5] == nArray[i-3]):
      nArray[i] = nArray[i-5] + 1

print(nArray[n])
