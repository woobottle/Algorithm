n = int(input())
arr = []
for i in range(n) :
  arr.append((int(input()), i))

sorted_arr = sorted(arr)

answer = 0
# 정렬한 상태의 인덱스에서 정렬전의 인덱스를 빼는것
for i in range(n) :
  answer = max(sorted_arr[i][1] - i + 1, answer)

print(answer)
