import sys

d = {}
for i in "abcdefghijklmnopqrstuvwxyz":
  d[i] = 0

w = sys.stdin.readline()
while w:
  for i in w:
    if i == "\n":
      continue
    elif i == " ":
      continue
    d[i] += 1
  w = sys.stdin.readline()

answer = ""
t = 0
for i in d.keys():
  if t < d[i]:
    t = d[i]
    answer = ""
    answer += i
  elif t == d[i]:
    answer += i

print(answer)