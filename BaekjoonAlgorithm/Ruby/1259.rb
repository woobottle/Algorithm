while true
  number = gets.chomp
  break if number == "0"
  number_array = number.split("")
  puts number_array == number_array.reverse ? "yes" : "no"
end