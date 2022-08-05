# 시험 점수

min_s = list(map(int, input().split()))
man_s = list(map(int, input().split()))
min_t, man_t = 0, 0

for i in range(0, 4):
  min_t += min_s[i]
  man_t += man_s[i]

if min_t > man_t:
  print(min_t)
elif min_t < man_t:
  print(man_t)
else:
  print(min_t)