while True :
  n = int(input())
  if(n == -1) :
    break
  l = [0] * (n+1)
  l[1] = 1
  for i in range(2, int(n ** 0.5) + 1) :
    if(n % i == 0):
      l[i] = 1
      l[n//i] = 1
  s = 1
  answer = "1"
  for i in range(2, n) :
    if(l[i] == 1) :
      s += i
      answer += " + " + str(i)
  if(n == s) :
    print(str(n) + " = " + answer)
  else :
    print(str(n) + " is NOT perfect.")