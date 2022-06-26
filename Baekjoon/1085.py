x, y, w, h = map(int, input().split())

if w-x > x:
  s_x = x
else:
  s_x = w-x

if h-y > y:
  s_y = y
else:
  s_y = h-y

print(min(s_x, s_y))

#아래는 틀린답
# if s_x >= s_y and x > s_y and y > s_y:
#   print(s_y)

# elif s_x < s_y and x > s_x and y > s_x:
#   print(s_x)

# elif s_y > x and s_x > x:
#   print(x)

# elif s_x > y and s_y > y:
#   print(y)