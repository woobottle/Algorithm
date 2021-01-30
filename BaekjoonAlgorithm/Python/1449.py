global L 
N, L = map(int, input().split())
holes = sorted(list(map(int,input().split())))

start = 0
tape_count = 0

def calc_start(h) :
  i = 0
  interval = 0
  while i < len(h) - 1 :
    if interval + (h[i+1] - h[i]) < L :
      interval += (h[i+1] - h[i])
      i += 1
    else : 
      break
  return i

while start < len(holes) :
  start = start + calc_start(holes[start:]) + 1
  tape_count += 1


print(tape_count)