first = int(input())
count = 0
new = first

while(1):
  ten = new%10
  one = new//10 + ten
  ten *= 10
  if one >= 10:
    one %= 10
    
  new = ten+one
  count += 1
  if new == first:
    break

print(count)
