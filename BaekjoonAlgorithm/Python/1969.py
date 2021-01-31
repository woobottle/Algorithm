from collections import Counter
from operator import itemgetter
N, M = map(int, input().split())
l = []
for _ in range(N) :
  l.append(input())

answer = ""
count = 0

for j in range(M) :
  temp = []
  for i in range(N) :
    temp.append(l[i][j])
  temp_dict= dict(Counter(temp).most_common())
  letters = sorted(temp_dict.items(), key=lambda kv: (-kv[1], kv[0]))  
  answer += letters[0][0]
  count += (sum(temp_dict.values()) - temp_dict[letters[0][0]])

print(answer)
print(count)
