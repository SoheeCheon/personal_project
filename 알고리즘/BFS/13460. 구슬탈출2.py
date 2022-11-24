from collections import deque

# 세로, 가로 값이 들어온다.
N, M = map(int, input().split())

miro = [input() for _ in range(N)]
visit = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

que = deque([])
for n in range(N):
    rx, ry, bx, by = 0, 0, 0, 0
    for m in range(M):
        if miro[n][m] == 'R':
            rx, ry = n, m

        elif miro[n][m] == 'B':
            bx, by = n, m

    # 빨간 구슬, 파란 구슬, 거리의 값을 que에 담아놓는다.
    que.append((rx, ry, bx, by, 1))
    visit[rx][ry][bx][by] = 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(x, y, dx, dy):
    cnt = 0
    # 도착지점 이거나 벽 전까지 진행한다.
    while miro[x+dx][y+dy] != '#' and miro[x][y] != '0':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs():
    while que:
        rx, ry, bx, by, depth = que.popleft()
        # 이동횟수가 10번이 넘어가면 -1 리턴
        if depth > 10:
            break

        for idx in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[idx], dy[idx])
            nbx, nby, bcnt = move(bx, by, dx[idx], dy[idx])

            if miro[nrx][nry] == 'O':
                print(depth)
                return

            # 두가지 공이 겹쳤을 때
            if nrx == nbx and nry == nby:
                # 이동거리가 많은 것을 한칸 뒤로, 이동거리가 많은게 뒤늦게 이동한 것이므로
                if rcnt > bcnt:
                    nrx -= dx[idx]
                    nry -= dy[idx]
                else:
                    nbx -= dx[idx]
                    nby -= dy[idx]

            # 방문하지 않았다면 큐에 추가하고
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = 1
                que.append((nrx, nry, nbx, nby, depth+1))

    print(-1)


bfs()