# 제로
# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

# 정답
import sys

n = int(sys.stdin.readline())
money = []
total = 0

for i in range(n):
  num = int(input())
  if num != 0:
    money.append(num)
  else:
    money.pop(len(money)-1)
  
for i in money:
  total += i

print(total)


# 시간초과로 오답 (답은 맞는듯?)
import sys

n = int(sys.stdin.readline())
money = [int(sys.stdin.readline()) for _ in range(n)]
total = 0

 while(1):
   if 0 in money:
     index = money.index(0)
     money.pop(index)
     money.pop(index-1)
   else:
     break

for i in money:
  total += i

print(total)
               