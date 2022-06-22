n = 9
max = 0
index = 0
list = [int(input()) for _ in range(n)]

for i in range(n):
  if list[i] > max:
    max = list[i]
    index = i+1

print(max)
print(index)