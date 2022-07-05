import sys
sys.setrecursionlimit(10 ** 9)


N = int(input())
lst = []
max_height = 0
for _ in range(N):
    row = list(map(int, input().split()))
    lst.append(row)
    for i in range(N):
        max_height = max(row[i], max_height)


def dfs(ci, cj, height):
    global visit

    visit[ci][cj] = 1

    for idx in range(4):
        ni = ci + di[idx]
        nj = cj + dj[idx]
        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and lst[ni][nj] > height:
            dfs(ni, nj, height)



# 안전한 지역을 구하기
# 상하좌우만 인접한 것으로 인정
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 안전한 영역의 갯수를 최대로
# 0 ~ 최대 높이 전 까지
ans = 0
for rain in range(max_height):
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and lst[i][j] > rain:
                dfs(i, j, rain)
                cnt += 1

    ans = max(cnt, ans)

print(ans)