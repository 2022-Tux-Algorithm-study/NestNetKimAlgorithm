# 백대열
# 유클리드 호제법 사용
# 참고: https://codingpractices.tistory.com/entry/Python-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EB%9E%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0

import sys

n, m = map(int, sys.stdin.readline().split(':'))

a = n
b = m

while m != 0:
    n, m = m, n % m

print(str(a//n) + ":" + str(b//n))