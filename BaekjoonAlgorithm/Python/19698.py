n,w,h,l = map(int,input().split())

s = (w // l) * (h // l)
print(min(n, s))