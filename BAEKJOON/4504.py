n = int(input())
list = []
i = 0


while(1):
  list.append(int(input()))
  if list[i] == 0:
    break;
  i += 1
  

for i in range(len(list)-1):
  if list[i]%n == 0:
    print(str(list[i]) + ' is a multiple of ' + str(n) + '.')
  else:
    print(str(list[i]) + ' is NOT a multiple of ' + str(n) + '.')