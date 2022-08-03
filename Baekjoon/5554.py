# 심부름 가는 길

time = [int(input()) for _ in range(4)]
y = time[0] + time[1] + time[2] + time[3]
x = y//60
y -= x*60

print(x)
print(y)