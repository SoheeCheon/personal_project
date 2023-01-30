from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(maps, visited, x, y):
    N = len(maps)
    M = len(maps[0])

    que = deque()
    que.append((x, y))
    ssum = int(maps[x][y])
    visited[x][y] = 1
    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 범위안에 있고 바다가 아니며 방문하지 않았을 경우, 큐에 넣고 합계를 갱신한다.
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = 1
                ssum += int(maps[nx][ny])

    return ssum


def solution(maps):
    answer = []

    N = len(maps)
    M = len(maps[0])
    visit = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 바다거나 방문했을 경우는 넘긴다.
            if maps[i][j] == "X" or visit[i][j] == 1:
                visit[i][j] = 1
                continue
            else:
                answer.append(bfs(maps, visit, i, j))
    # 값이 들어가 있으면 정렬된 값을 리턴하고 아니면 -1를 리턴한다.
    return sorted(answer) if len(answer) else [-1]