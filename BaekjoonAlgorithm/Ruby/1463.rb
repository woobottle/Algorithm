def check n
  array = Array.new(n+1, 0)
  (2..n).each do |number|
    array[number] = array[number-1] + 1
    if number % 3 == 0
      array[number] = [array[number], array[number/3]+1].min
    elsif number % 2 == 0
      array[number] = [array[number], array[number/2]+1].min
    end
  end
  array[n]
end
n = gets.to_i
print check(n) 