# 오각형, 오각형, 오각형...

n = int(input())
five = 5

for i in range(2, n+1):
  five += i * 3 + 1
  
print(five % 45678)