str = input()
count = 1

if str == ' ':
  count = 0

for i in range(0, len(str)):
  if str[i] == ' ':
    if i == 0 or i == len(str)-1:
      continue
    else:
      count += 1

print(count)