# 모음의 개수

word = list(input())
count = 0

for i in word:
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    count += 1

print(count)