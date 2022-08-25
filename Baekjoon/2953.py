# 나는 요리사다

n, m = 5, 4
score = []
for i in range(n):
  a, b, c, d = map(int, input().split())
  score.append(a+b+c+d)

best = max(score)
winner = score.index(best)

print(winner+1, best)

