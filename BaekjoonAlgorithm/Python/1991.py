n = int(input())
graph = {}

def pre_order(node) :
  if node != "." : 
    print(node, end = "")
    pre_order(graph[node][0])
    pre_order(graph[node][1])

def in_order(node) :
  if node != "." :
    in_order(graph[node][0])
    print(node, end ="")
    in_order(graph[node][1])

def post_order(node) :
  if node != ".":
    post_order(graph[node][0])
    post_order(graph[node][1])
    print(node, end="")

for _ in range(n) :
  root, left, right = input().split()
  graph[root] = [left, right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')
