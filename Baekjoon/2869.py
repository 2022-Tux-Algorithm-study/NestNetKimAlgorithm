# 달팽이는 올라가고 싶다

l, n, t = map(int, input().split())

d = l-n
count = (t-(l-d))//d

if (t-(l-d))%d != 0:
  count += 1

print(count)
