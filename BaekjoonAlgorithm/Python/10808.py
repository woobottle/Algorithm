s = input()
l = [0] * 26

for i in range(len(s)):
  l[ord(s[i]) - 97] += 1

print("".join(str(i) + " " for i in l))
