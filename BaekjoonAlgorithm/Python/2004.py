# 팩토리얼 계산법들 익숙해지기
def number_of_divider(n, k) :
  count = 0
  while n != 0 :
    count += n // k
    n //= k
  return count

n,m = map(int, input().split())
print(min((number_of_divider(n, 2) - number_of_divider(m, 2) - number_of_divider(n-m, 2)), (number_of_divider(n, 5) - number_of_divider(m, 5) - number_of_divider(n-m, 5))))
