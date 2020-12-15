s = ['A', 'B', 'C']
c = ['B', 'A', 'B', 'C']
h = ['C', 'C', 'A', 'A', 'B', 'B']

t = int(input())
l = input()

ss, cs, hs = 0, 0, 0
for i in range(len(l)):
  if l[i] == s[i%3]:
    ss += 1
  if l[i] == c[i%4]:
    cs += 1
  if l[i] == h[i%6]:
    hs += 1

score = [ss, cs, hs]
score.sort(reverse=True)
print(score[0])
if score[0] == ss :
  print('Adrian')
if score[0] == cs:
  print('Bruno')
if score[0] == hs:
  print('Goran')
