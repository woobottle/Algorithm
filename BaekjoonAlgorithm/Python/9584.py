import sys 

s = input()
# s 에서 * 인덱스 추출
sl = list(s)
si = []
for i in range(len(sl)) :
  if(sl[i] == '*') :
    si.append(i)

count = 0
answer = []
for _ in range(int(input())) :
  ss = input()
  # 비교구문, 카운팅
  ssl = list(ss)
  flag = 0
  for i in range(len(ssl)) :
    if(i in si) :
      continue
    else :
      if(ssl[i] != sl[i]) :
        flag = 1
        break
  if(flag == 0) :
    count += 1
    answer.append(ss)

print(count)
for i in answer : print(i)