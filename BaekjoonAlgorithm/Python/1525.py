from collections import deque

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

def check(array) :
  if("".join(array) == "123456780") :
    return True
  return False

def bfs(array) :
  q = deque()
  q.append(array)
  value_dict["".join(array)] = 0
  while q :
    temp_array = q.popleft()
    c_x = temp_array.index("0") // 3
    c_y = temp_array.index("0") % 3
    for i in range(4) :
      n_x = c_x + mx[i]
      n_y = c_y + my[i]
      if(0<= n_x < 3 and 0 <= n_y < 3) :
        curr_node = temp_array.index("0")
        next_node = n_x * 3 + n_y
        s_array = temp_array[:]
        s_array[curr_node], s_array[next_node] = s_array[next_node], s_array[curr_node]
        if(not "".join(s_array) in value_dict) :
          q.append(s_array)
          value_dict["".join(s_array)] = (value_dict.get("".join(temp_array)) + 1)
          
s_list = []
value_dict = {}

for _ in range(3) :
  for i in list(input().split()) : s_list.append(i)

bfs(s_list)

if("123456780" in value_dict) :
  print(value_dict.get("123456780"))
else :
  print(-1)