import sys

a = int(sys.stdin.readline())
array = [1, 0, 0]

for i in range(a):
  numbers = sys.stdin.readline().strip().split()
  index_1 = int(numbers[0]) - 1 
  index_2 = int(numbers[1]) - 1
  temp = array[index_1]
  array[index_1] = array[index_2]
  array[index_2] = temp

print(array.index(1) + 1)
