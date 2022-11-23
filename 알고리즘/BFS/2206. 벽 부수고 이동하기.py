from collections import deque
import copy

N, M = map(int, input().split())
arr = []

# 벽을 부시는 여부를 3차원 배열로 감지한다.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# 0,0 에서 시작하기 때문에 미리 방문 처리
visited[0][0][0] = 1

for i in range(N):
    arr.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    que = deque([])
    que.append((x, y, z))

    while que:
        cx, cy, cz = que.popleft()
        if cx == N -1 and cy == M - 1:
            return visited[cx][cy][cz]

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not(0 <= nx < N and 0 <= ny < M):
                continue

            # 범위안이고 아직 벽을 부수지 않았다면
            if arr[nx][ny] == 1 and cz == 0:
                visited[nx][ny][1] = visited[cx][cy][0] + 1
                que.append((nx, ny, 1))
            # 벽이 아니고 한번도 방문하지 않았다면
            elif arr[nx][ny] == 0 and visited[nx][ny][cz] == 0:
                visited[nx][ny][cz] = visited[cx][cy][cz] + 1
                que.append((nx, ny, cz))
    return -1


print(bfs(0,0,0))