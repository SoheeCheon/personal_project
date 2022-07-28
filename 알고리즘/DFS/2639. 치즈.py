import copy
import sys
sys.setrecursionlimit(10**9)

# 세로, 가로의 값이 들어온다
n, m = map(int, input().split())

cheess = []
cheess_cnt = 0
time = 0
for _ in range(n):
    lst = list(map(int, input().split()))
    # 처음에 치즈의 갯수를 미리 세둔다.
    cheess_cnt += lst.count(1)

    cheess.append(lst)

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(ci, cj):
    global copy_cheess, delete_cheess, cheess

    for di, dj in delta:
        ni = ci + di
        nj = cj + dj
        if time <= ni < n - time and time <= nj < m - time and visit[ni][nj] == 0:
            if cheess[ni][nj] and copy_cheess[ni][nj]:
                copy_cheess[ni][nj] = 0
                delete_cheess += 1
                visit[ni][nj] = 1
            else:
                visit[ni][nj] = 1
                dfs(ni, nj)

ans = 0
while cheess_cnt > 0:
    # 방문 위치를 초기화하고 치즈의 겉표면이 녹았는지 확인하기 위해 cheess 와 copy_cheess를 비교하여 확인
    visit = [[0] * m for _ in range(n)]
    copy_cheess = copy.deepcopy(cheess)
    delete_cheess = 0
    # 외각은 항상 비어있으므로
    dfs(time, time)

    # 만약 남은 치즈의 갯수와 현재 치즈의 갯수가 같다면 갱신
    if delete_cheess == cheess_cnt:
        ans = cheess_cnt

    cheess_cnt -= delete_cheess
    time += 1

    cheess = copy.deepcopy(copy_cheess)

print(time)
print(ans)

