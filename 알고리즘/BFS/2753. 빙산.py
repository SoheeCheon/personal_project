from collections import deque

# 세로, 가로 순으로 값이 들어온다.
N, M = map(int, input().split())

# 빙산의 정보
ice = [list(map(int, input().split())) for _ in range(N)]

# 지난 년수와 빙하의 덩어리 갯수를 저장할 변수
year = 0
cnt = 0

dn = [0, 0, 1, -1]
dm = [1, -1, 0, 0]


def bfs(x, y):
    global visit
    que = deque([])
    que.append((x, y))
    visit[x][y] = 1
    while que:
        cx, cy = que.popleft()
        for idx in range(4):
            nx = cx + dn[idx]
            ny = cy + dm[idx]
            # 근처에 빙하가 있다면 계속 탐색
            if ice[nx][ny] and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                que.append((nx, ny))

            # 얼음을 녹일 갯수를 세는중
            elif ice[nx][ny] == 0:
                count[cx][cy] += 1

    return 1


while 1:
    # 덩어리가 몇개 있는지 BFS 탐색
    visit = [[0] * M for _ in range(N)]
    count = [[0] * M for _ in range(N)]
    result = []
    for n in range(N):
        for m in range(M):
            if ice[n][m] and visit[n][m] == 0:
                result.append(bfs(n, m))
    # 녹은 빙하 갱신
    for n in range(N):
        for m in range(M):
            ice[n][m] -= count[n][m]
            if ice[n][m] < 0:
                ice[n][m] = 0

    # 덩어리가 한개인채로 녹아버린다면 0을 출력
    if len(result) == 0:
        print(0)
        break
    elif len(result) >= 2:
        print(year)
        break

    year += 1
