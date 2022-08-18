# 단어 공부
# 가장 많이 사용된 알파벳을 대문자로 출력
# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력

import sys

n = sys.stdin.readline()
n = list(n.upper())
n.pop(len(n)-1)

count = [0] * 26

for i in n:
  count[ord(i)-65] += 1
  
m = max(count)

# filter 사용해서 여려개 index 값 찾기
index = list(filter(lambda x: count[x] == m, range(len(count))))

if len(index) > 1:
  print('?')

else:
  print(chr(index[0] + 65))
