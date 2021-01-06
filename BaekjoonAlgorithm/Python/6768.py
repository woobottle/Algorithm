import itertools
n = int(input())
list = set()
for i in itertools.combinations(range(n-1), 3):
  list.add(i)
print(len(list))
