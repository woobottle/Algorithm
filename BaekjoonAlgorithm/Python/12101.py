l = []
l.append([])
l.append(["1"])
l.append(["1+1", "2"])
l.append(["1+1+1", "2+1", "1+2", "3"])

for i in range(4,11) :
  s = [i + "+3" for i in l[i-3]] + [i + "+2" for i in l[i-2]] + [i + "+1" for i in l[i-1]]
  l.append(s)


n,k = map(int, input().split())
if(k > len(l[n])) : print("-1")
else : print(sorted(l[n])[k-1])