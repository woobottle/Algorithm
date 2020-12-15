l = []
for _ in range(8):
  l.append(int(input()))
m = list(l)
m.sort()

a = []
b = 0
for i in range(3,8) :
  b += m[i]
  a += str(l.index(m[i]) + 1)
a.sort()
print(b)
print("".join(i + " " for i in a))
