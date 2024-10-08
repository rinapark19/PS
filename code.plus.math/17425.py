import sys

MAX = 1000000

f_list = [1] * (MAX + 1)
g_list = [0] * (MAX + 1)

# 약수의 합 리스트를 채우는 부분
for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX: # 2의 배수들에 전부 2 더해 주고, 3의 배수들에 전부 3 더해 주고...
        f_list[i*j] += i
        j += 1

for i in range(1, MAX+1): # 약수의 합 리스트를 이용해 전체 합 리스트를 구한다
    g_list[i] = g_list[i-1] + f_list[i]

n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    print(g_list[num])