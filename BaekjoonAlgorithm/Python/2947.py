import sys

def bubble(array) :
  if(array == [1,2,3,4,5]) : return
  for i in range(0, len(array) - 1 ):
    for j in range(i, len(array)) :
      if(array[i] > array[j]):
        array[j], array[i] = array[i], array[j]
        print("".join(str(i) + " " for i in array))
  bubble(array)

l = list(map(int, sys.stdin.readline().split(" ")))
bubble(l)
