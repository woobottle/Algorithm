import sys

array = [int(x) for x in sys.stdin.readline().split(" ")]
array.sort()
a = array[0]
b = array[1]

print(int((a+b) * ((abs(b-a)+1)/2)))