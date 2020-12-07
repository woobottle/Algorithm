number_array = [64, 32, 16, 8, 4, 2, 1]
count = 0
input_number = int(input())

while input_number != 0:
  for num in number_array:
    if input_number >= num:
      input_number -= num
      break
  count += 1

print(count)

# x = int(input())
# bin_x = bin(x)[2:]
# count = 0
# for num in bin_x:
#   count += int(num)
# print(count)
