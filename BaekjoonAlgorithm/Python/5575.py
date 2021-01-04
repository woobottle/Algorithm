from datetime import datetime, timedelta
year = 2021
month = 1
day = 1

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a1 = datetime(year, month, day, a[0], a[1], a[2])
a2 = datetime(year, month, day, a[3], a[4], a[5])
a2Ma1 = (a2-a1).seconds
aHours = a2Ma1 // 3600
a2Ma1 %= 3600
aMinutes = a2Ma1 // 60
a2Ma1 %= 60
aSeconds = a2Ma1
print(aHours, aMinutes, aSeconds)
b1 = datetime(year, month, day, b[0], b[1], b[2])
b2 = datetime(year, month, day, b[3], b[4], b[5])
b2Mb1 = (b2-b1).seconds
bHours = b2Mb1 // 3600
b2Mb1 %= 3600
bMinutes = b2Mb1 // 60
b2Mb1 %= 60
bSeconds = b2Mb1
print(bHours, bMinutes, bSeconds)
c1 = datetime(year, month, day, c[0], c[1], c[2])
c2 = datetime(year, month, day, c[3], c[4], c[5])
c2Mc1 = (c2-c1).seconds
cHours = c2Mc1 // 3600
c2Mc1 %= 3600
cMinutes = c2Mc1 // 60
c2Mc1 %= 60
cSeconds = c2Mc1
print(cHours, cMinutes, cSeconds)
