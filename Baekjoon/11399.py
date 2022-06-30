n = int(input())
time = list(map(int, input().split()))
total = 0

time.sort()

for i in range(0, n):
  total += time[i] * (n-i)
print(total)
