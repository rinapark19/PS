# 에라토스테네스의 체 이용

import sys

MAX = 1000000

e = [1] * (MAX + 1)

e[0] = 0
e[1] = 0

for i in range(2, MAX + 1):
    j = 2
    while i * j <= MAX:
        e[i*j] = 0
        j += 1

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if e[i] == 1:
        print(i)