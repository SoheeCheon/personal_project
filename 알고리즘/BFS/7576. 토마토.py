from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs():
    while start:
        i, j = start.popleft()
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if 0 <= ni < N  and 0 <= nj < M and box[ni][nj] == 0:
                start.append((ni, nj))
                box[ni][nj] = box[i][j] + 1


start = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            start.append((i, j))

bfs()

maxNum = 0
# 익지 않은 토마토가 있을경우
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    maxNum = max(maxNum, max(i))
print(maxNum-1)
