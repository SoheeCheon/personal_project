import sys
sys.setrecursionlimit(10**9)

# 세로, 가로, 직사각형의 갯수
N, M, K = map(int, input().split())

arr = [[1] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for cx in range(x1, x2):
        for cy in range(y1, y2):
            arr[cy][cx] = 0

lst = []
cnt = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(ci, cj):
    global area
    visit[ci][cj] = 1
    area += 1

    for i in range(4):
        ni = ci + di[i]
        nj = cj + dj[i]
        if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and arr[ni][nj] == 1:
            dfs(ci, cj)


for x in range(M):
    for y in range(N):
        if arr[y][x] == 1 and visit[y][x] == 0:
            cnt += 1
            area = 0
            dfs(y, x)
            lst.append(area)

print(cnt)
print(*lst)
