n = int(input())
k = int(input())
l = sorted(list(map(int,input().split())))
answer = []
for i in range(0,len(l)-1) :
  answer.append(l[i+1] - l[i])

answer.sort(reverse=True)
print(sum(answer[k-1:]))
# 1 3 6 6 7 9
# 2 3 0 1 2 
# 한 집중국이[1, 3] 구간을 수신하고, 다른 집중국이 [6, 9] 구간을 수신한다. 따라서 두 영역 길이의 합은 2 + 3으로 5가 된다.
