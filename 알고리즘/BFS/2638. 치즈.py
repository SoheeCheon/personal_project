from collections import deque
import copy

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 8방향을 찾아보는 경우
ax = [-1, -1, 0, 1, 1, 1, 0, -1]
ay = [0, 1, 1, 1, 0, -1, -1, -1]

time = 0


def check_around(cx, cy):
    # 2로 표시된 곳은 삭제될 치즈
    visit = [[0] * M for _ in range(N)]
    que = deque([(cx, cy)])
    visit[cx][cy] = 1
    copy_cheese = copy.deepcopy(cheese)
    while que:
        now_x, now_y = que.popleft()
        for idx in range(8):
            nx = now_x + ax[idx]
            ny = now_y + ay[idx]
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if visit[nx][ny] == 0 and copy_cheese[nx][ny]:
                visit[nx][ny] = 1
                que.append((nx, ny))

                cnt = 0
                for i in range(4):
                    qx = nx + dx[i]
                    qy = ny + dy[i]
                    if not (0 <= qx < N and 0 <= qy < M):
                        continue

                    if copy_cheese[qx][qy] == 0:
                        cnt += 1

                if cnt >= 2:
                    cheese[nx][ny] = 0
                break

    return


for n in range(N):
    for m in range(M):
        if cheese[n][m] == 1:
            check_around(n, m)
            time += 1

            for lst in cheese:
                if 1 in lst:
                    break

