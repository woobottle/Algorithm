E,S,M = map(int, input().split())

earth, sun, moon = 1, 1, 1
year = 1

while True :
  if(earth == E and sun == S and moon == M) : break
  earth = (earth + 1) % 16
  if earth == 0 : earth = 1
  sun = (sun + 1) % 29
  if sun == 0: sun = 1
  moon = (moon + 1) % 20
  if moon == 0: moon = 1
  year += 1

print(year)
