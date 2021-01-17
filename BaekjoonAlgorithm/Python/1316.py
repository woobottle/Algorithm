n = int(input())
count = 0 

for _ in range(n) :
  flag = True
  s = set()
  case = input()
  last_word = case[0]
  s.add(last_word)
  for i in range(1, len(case)) :
    char = case[i]
    if(last_word != char):
      if(char in s):
        flag = False
        break
      else :
        s.add(char)
        last_word = char
  if flag :
    count += 1
  
print(count)

# result = 0
# for i in range(int(input())):
#     word = input()
#     print(sorted(word, key=word.find))
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)
