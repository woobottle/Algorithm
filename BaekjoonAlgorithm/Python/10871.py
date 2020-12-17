n,x = map(int, input().split())
l = list(map(int, input().split()))

s = ""
for i in l :
  if(i < x) :
    s += (str(i) + " ")

print(s)