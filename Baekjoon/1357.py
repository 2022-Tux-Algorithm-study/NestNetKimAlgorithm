# 뒤집힌 덧셈
# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램

x, y = map(str, input().split())
x, y = int(x[::-1]), int(y[::-1])

total = str(x+y)
total = total[::-1]

print(int(total))
