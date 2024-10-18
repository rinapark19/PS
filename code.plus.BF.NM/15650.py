import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]
answer = list(combinations(N_list, M))
answer.sort()

for a in answer:
    a = list(a)
    print(' '.join(list(map(str, a))))