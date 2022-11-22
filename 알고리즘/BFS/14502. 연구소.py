from collections import deque
import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs():
    global ans
    que = deque([])
    # 바이러스의 시작 시점을 넣어준다
    for qi in range(N):
        for qj in range(M):
            if arr[qi][qj] == 2:
                que.append((qi, qj))

    copy_arr = copy.deepcopy(arr)
    while que:
        ci, cj = que.popleft()
        for idx in range(4):
            ni = ci + di[idx]
            nj = cj + dj[idx]
            if 0 <= ni < N and 0 <= nj < M and copy_arr[ni][nj] == 0:
                que.append((ni, nj))
                copy_arr[ni][nj] = 2

    cnt = 0
    for n in range(N):
        cnt += copy_arr[n].count(0)

    ans = max(ans, cnt)


def wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return

    for n in range(N):
        for m in range(M):
            if arr[n][m] == 0:
                arr[n][m] = 1
                wall(wall_cnt+1)
                arr[n][m] = 0


wall(0)
print(ans)