s = "0b" + input()
target = int(s, 2) * 17
print(bin(target).replace('0b', ''))
