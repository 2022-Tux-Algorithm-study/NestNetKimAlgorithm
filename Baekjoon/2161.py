# 카드1
# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.

card = [n for n in range(1, int(input())+1)]

while(1):
  if len(card) == 1:
    break
  print(card[0], end = ' ')
  card.pop(0)
  num = card[0]

  card.pop(0)
  card.append(num)

print(card[0], end = ' ')
  
