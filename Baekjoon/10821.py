# 정수의 개수

num = input()
count = 1

for i in num:
  if i == ',':
    count += 1

print(count)