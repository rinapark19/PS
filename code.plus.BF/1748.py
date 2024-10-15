import sys
input = sys.stdin.readline
answer = 0
n = str(int(input()))
N = len(n)
n = int(n)

for i in range(1, N):
    answer += 9 * 10 ** (i-1) * i

answer += N * (n - 10 ** (N-1) + 1)
print(answer)