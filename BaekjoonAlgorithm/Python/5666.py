import sys 

while True :
  try :
    h, p = map(int, input().split())
    print('%.2f'%(h/p))
  except EOFError:
    break

