from collections import deque
import math

N, L, R = map(int, input().split())

national = [list(map(int, input().split())) for _ in range(N)]

# 오, 좌, 상, 하 순으로 탐색
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(cx, cy):
    global visit
    cnt = 1
    total = national[cx][cy]
    que = deque([])
    que.append((cx, cy))
    visit[cx][cy] = 2
    near_national = [(cx, cy)]
    while que:
        cur_x, cur_y = que.popleft()
        for idx in range(4):
            nx = cur_x + dx[idx]
            ny = cur_y + dy[idx]
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            if visit[nx][ny] == 0 and L <= abs(national[cur_x][cur_y] - national[nx][ny]) <= R:
                que.append((nx, ny))
                cnt += 1
                total += national[nx][ny]
                visit[nx][ny] = 1
                near_national.append((nx, ny))

    # 인접한 국가의 인구수를 나누는 문단
    person = math.floor(total/cnt)
    for change_x, change_y in near_national:
        national[change_x][change_y] = person

    return

day = 0
while 1:
    visit = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visit[x][y] == 0:
                bfs(x, y)

    flag = True
    for lst in visit:
        if lst.count(1) > 0:
            flag = False
            break

    if flag:
        print(day)
        break
    else:
        day += 1