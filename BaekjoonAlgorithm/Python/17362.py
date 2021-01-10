n = int(input())
s = n % 8

if(s == 1) : print(1)
elif(s == 2 or s == 0) : print(2)
elif(s == 3 or s == 7) : print(3)
elif(s == 4 or s == 6) : print(4)
elif(s == 5) : print(5)