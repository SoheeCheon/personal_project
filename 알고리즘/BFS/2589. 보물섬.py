from collections import deque

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
ans = 0
dn = [0, 0, 1, -1]
dm = [1, -1, 0, 0]


def bfs(x, y):
    global ans
    que = deque([])
    que.append((x, y))
    visit[x][y] = 1
    while que:
        cx, cy = que.popleft()
        for idx in range(4):
            nx = cx + dn[idx]
            ny = cy + dm[idx]
            if not( 0 <= nx < N and 0 <= ny < M):
                continue
            if visit[nx][ny] == 0 and arr[nx][ny] == 'L':
                visit[nx][ny] = visit[cx][cy] + 1
                ans = max(ans, visit[nx][ny])
                que.append((nx, ny))


for n in range(N):
    for m in range(M):
        if arr[n][m] == 'L':
            visit = [[0] * M for _ in range(N)]
            bfs(n, m)


print(ans - 1)
