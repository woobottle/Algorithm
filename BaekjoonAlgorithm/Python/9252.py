import sys
sys.setrecursionlimit(int(1e6))

def findLcs(arr_first, arr_second, arr_global) :
  for i in range(len(arr_first)):
    for j in range(len(arr_second)):
      if(arr_first[i] == arr_second[j]):
        arr_global[i][j] = arr_global[i-1][j-1] + 1
      else:
        arr_global[i][j] = max(arr_global[i-1][j], arr_global[i][j-1])
  return arr_global[len(arr_first)-1][len(arr_second)-1]

def getStr(x, y, arr_first, arr_second) :
  if x == -1 or y == -1 :
    return ""
  elif arr_first[x] == arr_second[y] :
    return getStr(x-1, y-1, arr_first, arr_second) + arr_first[x]
  else :
    if arr[x-1][y] < arr[x][y-1] :
      return getStr(x, y-1, arr_first, arr_second)
    else :
      return getStr(x-1, y, arr_first, arr_second)

first = list(input())
second = list(input())

arr = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

answer_len = findLcs(first, second, arr)
print(answer_len)
if answer_len != 0 :
  print(getStr(len(first)-1, len(second)-1, first, second))
