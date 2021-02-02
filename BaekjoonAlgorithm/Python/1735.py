def gcp(first, second) :
  if(second == 0) : return first
  return gcp(second, first % second)

a,b = map(int, input().split())
c,d = map(int, input().split())

gcp_body = gcp(b,d)

head = int((a * d) / gcp_body + (b * c) / gcp_body)
body = int(b * d / gcp_body)
gcp_answer = gcp(head, body)
print(int(head/gcp_answer), int(body/gcp_answer))