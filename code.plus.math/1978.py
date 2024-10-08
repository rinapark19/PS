# 에라토스테네스의 체 이용

import sys

MAX = 1000

e = [1] * (MAX + 1)

e[0] = 0
e[1] = 0

for i in range(2, MAX + 1):
    j = 2
    while i * j <= MAX:
        e[i*j] = 0
        j += 1

num = int(sys.stdin.readline())
n_list = map(int, sys.stdin.readline().split())

ans = 0
for n in n_list:
    if e[n] == 1:
        ans += 1

print(ans)