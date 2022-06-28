num = int(input())

rope = [int(input()) for _ in range(num)]
rope.sort()
max = 0

for i in range(0, num):
  w = rope[i] * (num - i)
  if w > max:
    max = w
  
print(max)