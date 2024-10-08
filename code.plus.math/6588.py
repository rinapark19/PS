import sys

# 에라토스테네스의 체 이용

MAX = 1000001
e = [1] * MAX

for i in range(3, int(MAX ** 0.5) + 1, 2):
    if e[i]: # i가 홀수인 소수
        for j in range(i*2, MAX, i):
            e[j] = 0 # 해당 소수의 배수인 것들을 모두 0으로 표시


while 1:
    k = int(sys.stdin.readline())
    if not k:
        break
    for i in range(3, int(k / 2) + 1, 2):
        if e[i] and e[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")