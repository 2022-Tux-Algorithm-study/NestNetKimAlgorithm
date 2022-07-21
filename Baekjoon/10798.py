word = [list(input()) for _ in range(5)]

for i in range(0, 15):
  for j in range(0, 5):
    if len(word[j]) < i+1:
      continue
    else:
      print(word[j][i], end='')

