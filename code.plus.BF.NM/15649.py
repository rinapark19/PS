import sys
input = sys.stdin.readline

from itertools import permutations

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]
answer = list(permutations(N_list, M))

for a in answer:
    a = list(a)
    print(' '.join(list(map(str, a))))