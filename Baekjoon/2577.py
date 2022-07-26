# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())
total = a*b*c
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while(1):
  
  n = total%10
  num[n] += 1
  
  if total < 10:
    break
    
  total = total // 10

for i in num:
  print(i)
  