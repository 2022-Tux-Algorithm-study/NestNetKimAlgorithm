n = int(input())
word = [input() for _ in range(n)]

word = list(set(word))  # set으로 중복 제거
word.sort()               # 사전 순 정렬
word.sort(key=len)     # 길이 순 정렬
  
for a in word:
  print(a)

