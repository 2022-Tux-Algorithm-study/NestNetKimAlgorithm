sen = input()
len = len(sen)//10

if len >= 1:
  for i in range(0, len):
    if i == 0:
      print(sen[0:10])
    else:
      print(sen[10*i:10*(i+1)])

  print(sen[10*len:])

else:
  print(sen[:])