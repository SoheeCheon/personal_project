N = int(input())

# 집이 있는 곳 : 1, 집이 없는 곳 0
arr = [list(map(int, input().strip())) for _ in range(N)]
# 방문처리
visited = [[0] * N for _ in range(N)]

cnt = 0
# 각 단지의 갯수를 셀 리스트
lst = []

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def dfs(ci, cj):
    global visited, ans

    # 방문하지 않은 곳이라면 ans를 갱신
    if not visited[ci][cj]:
        visited[ci][cj] = 1
        ans += 1

    # 델타탐색 실시
    for idx in range(4):
        ni = ci + di[idx]
        nj = cj + dj[idx]
        # 범위안이고 방문하지 않았고 집이있는 곳이라면 다음으로 탐색시작
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj]:
            dfs(ni, nj)


for i in range(N):
    for j in range(N):
        # 집이 있고 방문하지 않은곳이면 dfs 탐색 시작
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            ans = 0
            dfs(i, j)

            lst.append(ans)

print(cnt)

# 오름차순 정렬후 출력을 위해
lst.sort()

for l in lst:
    print(l)