# 테스트 케이스의 갯수
T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(cx, cy):
    house[cy][cx] = 0

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < M and 0 <= ny < N and house[ny][nx] == 1:
            dfs(nx, ny)


def bfs(cx, cy):
    global house
    queue = []
    queue.append((cx, cy))
    house[cy][cx] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and house[ny][nx] == 1:
                house[ny][nx] = 0
                queue.append((nx, ny))

    return


for t in range(1, T+1):
    # M: 가로, N: 세로, K: 배추의 위치 정보갯수
    M, N, K = map(int, input().split())

    house = [[0] * M for _ in range(N)]

    # 배추의 위치 정보 입력
    for _ in range(K):
        x, y = map(int, input().split())

        house[y][x] = 1

    ans = 0
    for y in range(N):
        for x in range(M):
            if house[y][x] == 1:
                bfs(x, y)
                ans += 1

    print(ans)

