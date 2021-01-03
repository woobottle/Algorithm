n = int(input())

# 둘의 곱을 최대공약수로 나누면 최소공배수

# 유클리드 호제법
# 최대공약수 구하는 식
def gcd(a,b) :
  while b != 0 :
    a,b = b, a%b
  return a

for i in range(n) :
  a,b = map(int, input().split())
  print(int(a*b/gcd(a,b)))