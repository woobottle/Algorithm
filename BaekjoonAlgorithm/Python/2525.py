from datetime import datetime, timedelta
a,b = map(int, input().split())
c = int(input())

now = datetime(2020,1,1,a,b)
cDelta = timedelta(minutes=c)
answer = (now+cDelta).strftime("%H %M").split()
print(int(answer[0]), int(answer[1]))

