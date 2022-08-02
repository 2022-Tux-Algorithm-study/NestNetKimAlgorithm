# 알파벳 개수

alph = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

word = list(input())

for i in word:
  alph[ord(i)-97] += 1

for i in alph:
  print(i, end=' ')