# DFS로 푸는 문제
# 2차원 배열에 배추를 표시하고, 방문하지 않은 배추면 DFS 시행해서 방문 체크, 이걸 전체 그래프에 실행

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 방문했던 배추일 경우 
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)

num_case = int(input())
for _ in range(num_case):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    count = 0
    for a in range(m):
        for b in range(n):
            # 한 그룹당 한 개만 1로 표시됨(주변은 -1)
            if graph[b][a] == 1:
                dfs(a, b)
                count += 1

    print(count)