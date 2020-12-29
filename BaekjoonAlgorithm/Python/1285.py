n = int(input())
l = []
for _ in range(n) :
  l.append(list(input()))

row_tail_count = 0
row_head_count = 0
column_tail_count = 0
column_head_count = 0

for i in range(n) :
  row_tail_count = l[i].count("T")
  row_head_count = l[i].count("H")
  if(row_tail_count > row_head_count) :
    for ii in range(n) :
      if(l[i][ii] == "T") : l[i][ii] = "H"
      else : l[i][ii] = "T"
  column_tail_count = [k[i] for k in l].count("T")
  column_head_count = [k[i] for k in l].count("H")
  if(column_tail_count > column_head_count):
    for jj in range(n):
      if(l[jj][i] == "T"): l[jj][i] = "H"
      else: l[jj][i] = "T"

print(l)
tail_count = 0
for i in range(n) :
  tail_count += l[i].count("T")
print(tail_count)
