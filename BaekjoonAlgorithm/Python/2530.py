from datetime import datetime, timedelta
a, b, c = map(int, input().split())
d = int(input())

now = datetime(2020, 1, 1, a, b, c)
cDelta = timedelta(seconds=d)
answer = (now+cDelta).strftime("%H %M %S").split()
print(int(answer[0]), int(answer[1]), int(answer[2]))
