import sys

def count(n,k) :
  count = n
  while n//k != 0 :
    s = n//k
    n -= s*k
    n += s
    count += s
  return count

# try :
#   while True :
#     n,k = map(int, input().split())
# except :
#   exit()

# 입력받은대로 출력하기
for line in sys.stdin :
  n, k = map(int, line.split())
  print(count(n, k))
