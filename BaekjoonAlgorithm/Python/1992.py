import sys 
answer = ""

def check(x, y, length) :
  for i in range(x, x+length) :
    for j in range(y, y+length) :
      if(graph[x][y] != graph[i][j]) :
        return False
  return True

def zip(x, y, length) :
  global answer
  if(check(x,y,length)) :
    answer += str(graph[x][y])
  else :
    answer += "("
    length //= 2 
    zip(x, y, length)
    zip(x, y+length, length)
    zip(x+length, y, length)
    zip(x+length, y+length, length)
    answer += ")"

n = int(sys.stdin.readline().strip())
graph = []

for _ in range(n) :
  graph.append(list(map(int, sys.stdin.readline().strip())))

zip(0, 0, n)
print(answer)
