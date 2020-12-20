n = int(input())
for i in range(n) :
  s = input().strip()
  count = 0
  count = s.count('a') + s.count('e') + s.count('i') + \
      s.count('o') + s.count('u') + s.count('A') + \
      s.count('E') + s.count('I') + s.count('O') + s.count('U')
  print(len(s)-count-s.count(' '), count)
