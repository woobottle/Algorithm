n = gets.chomp.to_i
min = n + 1;

for i in 0..n/5
  j = (n - i * 5) % 3 == 0 ? (n - i * 5) / 3 : n + 1
  if min > i + j
    min = i + j
  end
end

puts min == n + 1 ? -1 : min
