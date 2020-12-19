ay, am, ad = map(int, input().split())
by, bm, bd = map(int, input().split())

c = 0
if am > bm or (am == bm and ad > bd) :
  c = 1 

print(by - ay - c)
print(by - ay + 1)
print(by - ay)
