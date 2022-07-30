# 줄번호

n = int(input())
sen = [input() for _ in range(n)]

for i in range(0, len(sen)):
  print(str(i+1) + '. ' + sen[i])