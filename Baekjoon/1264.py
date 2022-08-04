# 모음의 개수

while(1):
  count = 0
  sen = list(input())
  if sen == ['#']:
    break
    
  for i in sen:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
      count += 1

  print(count)