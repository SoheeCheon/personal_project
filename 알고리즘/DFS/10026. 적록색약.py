import sys
sys.setrecursionlimit(10**9)

N = int(input())

# 상하좌우 탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 문자열로 올라온다.
lst = [input() for _ in range(N)]
visit = [[0] * N for _ in range(N)]
sick_visit = [[0] * N for _ in range(N)]


# 일반인의 구역 구분
def dfs(ci, cj, color):
    visit[ci][cj] = 1

    for idx in range(4):
        ni = ci + di[idx]
        nj = cj + dj[idx]
        # 방문하지 않고 색이 같으면
        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and lst[ni][nj] == color:
            dfs(ni, nj, color)


def sick_dfs(ci, cj, color):
    sick_visit[ci][cj] = 1

    for idx in range(4):
        ni = ci + di[idx]
        nj = cj + dj[idx]
        # 방문하지 않고 색이 같은것은 똑같으나 빨간색과 초록색일 때는 서로 통과는것까지
        if 0 <= ni < N and 0 <= nj < N and sick_visit[ni][nj] == 0:
            if lst[ni][nj] == color or color =='G' and lst[ni][nj] == 'R' or color == 'R' and lst[ni][nj] == 'G':
                sick_dfs(ni, nj, color)


cnt = 0
sick_cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            word = lst[i][j]
            dfs(i, j, word)
            cnt += 1
            if sick_visit[i][j] == 0:
                sick_dfs(i, j, word)
                sick_cnt += 1

print(cnt, sick_cnt)
