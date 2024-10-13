import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)] # DFS를 위해 방문 여부 확인용 배열 만듦

# 좌표 이동
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0

# 종이에서 가장 큰 값
max_val = max(map(max, arr))

def dfs(r, c, idx, total):
    global ans
    # 현재의 dfs에서 남은 블록이 모두 최댓값에 해당하더라도 현재 ans를 넘기지 못한다면 종료
    if ans >= total + max_val * (3 - idx):
        return
    
    # 4개의 블록 사용
    if idx == 3:
        # 현재 dfs 값과 이전까지의 최댓값 비교
        ans = max(ans, total)
        return

    # 4개의 블록 다 사용하지 않음
    else:
        # 방향
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 이동하려는 위치가 종이 안에 있고, 방문한 적 없음
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                # 만약 2개 블록 선택했다면(ㅗ 모양 블럭 탐색을 위해 따로 뺌)
                if idx == 1:
                    # 방문 확인
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total+ arr[nr][nc]) # 원래 좌표값 넣어주는 거
                    visit[nr][nc] = 0
                
                visit[nr][nc] = 1
                dfs(nr, nc, idx+1, total+arr[nr][nc])
                visit[nr][nc] = 0

for r in range(N):
    for c in range(M):
        # 방문 확인
        visit[r][c] = 1

        # DFS 호출 > ans 최댓값 구하기
        dfs(r, c, 0, arr[r][c])

        # 목적지 해제(백트래킹?)
        visit[r][c] = 0

print(ans)