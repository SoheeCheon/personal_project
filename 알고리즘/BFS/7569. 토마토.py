from collections import deque

# 가로, 세로, 높이
N, M, H = map(int, input().split())
boxes = []
que = deque([])

for h in range(H):
    box = [list(map(int, input().split())) for _ in range(M)]
    for m in range(M):
        for n in range(N):
            if box[m][n] == 1:
                # 가로 세로 높이 순으로 넣어준다.
                que.append((n,m,h))
    boxes.append(box)

# 3 방향 델타 탐색
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]


def bfs():
    while que:
        cx, cy, cz = que.popleft()
        for idx in range(6):
            nx = cx + dx[idx]
            ny = cy + dy[idx]
            nz = cz + dz[idx]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and boxes[nz][ny][nx] == 0:
                que.append((nx, ny, nz))
                boxes[nz][ny][nx] = boxes[cz][cy][cx] + 1


bfs()

# 날짜 계산
day = 0
for box in boxes:
    for arr in box:
        if arr.count(0):
            print(-1)
            exit(0)

        day = max(day, max(arr))

print(day - 1)