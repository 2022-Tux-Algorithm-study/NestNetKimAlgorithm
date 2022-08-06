# 방학 숙제

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a%c != 0:
  play = a//c + 1
else:
  play = a//c
if b%d != 0:
  if b//d+1 > play:
    play = b//d+1
else:
  if b//d > play:
    play = b//d

print(l - play)