from collections import deque

# 세로, 가로, 영역의 갯수
M, N, K = map(int, input().split())

arr = [[0] * N for _ in range(M)]
visit = [[0] * N for _ in range(M)]

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())

    # 영역을 채우는 중
    for j in range(sy, ey):
        for i in range(sx, ex):
            arr[j][i] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visit[x][y] = 1
    area = 1
    while que:
        cx, cy = que.popleft()
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0 and visit[nx][ny] == 0:
                que.append((nx, ny))
                visit[nx][ny] = 1
                area += 1

    return area


result = []
for m in range(M):
    for n in range(N):
        if arr[m][n] == 0 and visit[m][n] == 0:
            cnt = bfs(m, n)
            result.append(cnt)


result.sort()
print(len(result))
for a in result:
    print(a, end=" ")
