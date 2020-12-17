import copy
n = list(map(int, input().split()))
rn = sorted(copy.deepcopy(n))
if n == rn : print("Good")
else : print("Bad")
