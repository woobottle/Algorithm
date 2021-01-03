def gcd(a,b) :
  while b :
    a,b = b, a%b
  return a

a,b = map(int, input().split())
# 최대공약수 출력
print(gcd(a,b))
# 최소공배수 출력
print(int(a*b/gcd(a, b)))
