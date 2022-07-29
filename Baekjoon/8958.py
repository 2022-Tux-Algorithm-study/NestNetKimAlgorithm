OX 퀴즈

n = int(input())
check = [list(input()) for _ in range(n)]

for i in range(0, n):
  score, o = 0, 0
  for j in range(0, len(check[i])):
    if check[i][j] == 'X':
      o = 0
    elif check[i][j] == 'O':
      o += 1
      score += o

  print(score)