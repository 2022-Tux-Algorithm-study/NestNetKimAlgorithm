num = int(input())
order = list(map(int, input().split()))

# set은 중복 허용x, 순서x
order = list(set(order))
order.sort()

for i in order:
  print(i, end=' ')

# hm,, 이건 왜 틀렸지 
#for i in range(0, num - 1):
#   if i == 0:
#     print(order[i], end=' ')
  
#   elif order[i] != order[i-1]:
#     print(order[i], end=' ')