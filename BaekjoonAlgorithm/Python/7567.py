s = list(input())
i = 10
for k in range(1, len(s)) :
  if(s[k] != s[k-1]) :
    i += 10
  else :
    i += 5

print(i)