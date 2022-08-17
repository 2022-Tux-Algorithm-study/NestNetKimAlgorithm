# 베스트셀러
# 가장 많이 팔린 책의 제목을 출력

import sys

n = int(sys.stdin.readline())
book = [sys.stdin.readline() for _ in range(n)]
book.sort()

print(max(book, key = book.count))
