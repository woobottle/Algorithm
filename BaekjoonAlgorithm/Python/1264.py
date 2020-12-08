import sys

def checkSentence(str1):
  answerArray = ['a','e','i','o','u']
  strArray = [*str1]
  count = 0
  for char in strArray :
    if(char in answerArray):
      count += 1
  print(count)

while True :
  sentence = sys.stdin.readline().strip().lower()
  if sentence == "#" : break
  checkSentence(sentence)
