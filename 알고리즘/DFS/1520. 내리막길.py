import sys

sys.setrecursionlimit(10 ** 6)
# 세로, 가로 순으로 값이 들어온다.
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
visit = [[0] * N for _ in range(M)]

cnt = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def dfs(ci, cj):
    global cnt

    visit[ci][cj] = 1

    # 우하단에 도착하면 갯수 갱신후 빠져나감
    if ci == (M - 1) and cj == (N - 1):
        cnt += 1
        return

    for idx in range(4):
        ni = ci + di[idx]
        nj = cj + dj[idx]
        if 0 <= ni < M and 0 <= nj < N and visit[ni][nj] == 0 and arr[ci][cj] > arr[ni][nj]:
            # 현재위치보다 다음위치의 값이 작아야한다
            dfs(ni, nj)

dfs(0, 0)
print(cnt)