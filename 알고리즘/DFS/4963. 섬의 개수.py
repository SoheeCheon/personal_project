import sys
sys.setrecursionlimit(10**9)

def dfs(ci, cj):
    global visit
    visit[ci][cj] = 1

    for i in range(8):
        ni = ci + d_h[i]
        nj = cj + d_w[i]
        if 0 <= ni < h and 0 <= nj < w and visit[ni][nj] == 0 and lst[ni][nj] == 1:
            dfs(ni, nj)


def bfs(ci, cj):
    global visit
    queue = [[ci, cj]]
    visit[ci][cj] = 1

    while queue:
        now = queue.pop(0)

        for i in range(8):
            ni = now[0] + d_h[i]
            nj = now[1] + d_w[i]
            if 0 <= ni < h and 0 <= nj < w and visit[ni][nj] == 0 and lst[ni][nj] == 1:
                visit[ni][nj] = 1
                dfs(ni, nj)


while True:
    w, h = map(int, input().split())

    if not(w == 0 and h == 0):
        # 0은 바다, 1은 땅
        lst = [list(map(int, input().split())) for _ in range(h)]
        visit = [[0] * w for _ in range(h)]

        # 델타탐색
        d_w = [0, -1, -1, -1, 0, 1, 1, 1]
        d_h = [1, 1, 0, -1, -1, -1, 0, 1]

        cnt = 0
        for ch in range(h):
            for cw in range(w):
                if lst[ch][cw] == 1 and visit[ch][cw] == 0:
                    dfs(ch, cw)
                    cnt += 1

        print(cnt)
    else:
        break





