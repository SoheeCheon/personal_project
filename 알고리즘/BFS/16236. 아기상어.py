from collections import deque

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
x, y = 0, 0

for n in range(N):
    for m in range(N):
        if arr[n][m] == 9:
            x = n
            y = m
            break

size = 2

# 상어의 현재위치와 크기
def bfs(cur_x, cur_y, shark_size):
    eatable = []
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    que = deque([])
    que.append((cur_x, cur_y))
    visited[cur_x][cur_y] = 1
    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + di[i]
            ny = cy + dj[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # 상어가 지나갈수 있는 공간 구하기
                if arr[nx][ny] <= shark_size:
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cx][cy] + 1

                    # 상어가 먹을 수 있는 물고기 구하기
                    if arr[nx][ny] < shark_size and arr[nx][ny] != 0:
                        eatable.append((nx, ny, distance[nx][ny]))

    # 거리가 가까운 순, 위로 가까운 순, 왼쪽으로 가까운 순으로 정렬하여 반환한다.
    return sorted(eatable, key=lambda x: (-x[2], -x[0], -x[1]))


eat_cnt = 0
ans = 0

while 1:
    shark = bfs(x, y, size)

    # 더이상 먹을수 있는게 없다면
    if len(shark) == 0:
        break

    nx, ny, dis = shark.pop()

    # 물고기가 있는 칸과 상어가 있는 칸 모두 초기화
    arr[x][y], arr[nx][ny] = 0, 0
    x, y = nx, ny

    eat_cnt += 1
    ans += dis
    if eat_cnt == size:
        size += 1
        eat_cnt = 0


print(ans)