import sys 

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
sorted_array = sorted(array)
answer_list = []
checked = [False] * n
for i in array :
  for j in range(n) :
    if(sorted_array[j] == i and checked[j] == False):
      checked[j] = True
      answer_list.append(j)
      break

answer = ""
print(answer.join(str(i) + " " for i in answer_list))
