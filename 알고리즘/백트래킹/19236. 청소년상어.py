import copy

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]


board = [[] for _ in range(4)]
for j in range(4):
    lst = list(map(int, input().split()))
    fish = []
    for i in range(4):
        # 번호, 벡터 순으로
        fish.append([lst[2*i], lst[2*i+1]])
    board[j] = fish

ans = 0


def dfs(ci, cj, cnt, board):
    global ans
    cnt += board[ci][cj][0]
    ans = max(cnt, ans)
    board[ci][cj][0] = 0

    # 물고기 움직임
    # 1번 부터 16번까지
    for f in range(1, 17):
        f_i, f_j = -1, -1
        # 해당하는 물고기의 위치를 받는다.
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == f:
                    f_i, f_j = i, j
                    break
        if f_i == -1 or f_j == -1:
            continue
        # 해당 물고기의 방향을 받아서
        f_v = board[f_i][f_j][1]

        # 이동가능한 방향으로 이동
        for i in range(8):
            nv = (f_v + i) % 8
            ni = f_i + di[nv]
            nj = f_j + dj[nv]
            # 범위안이 아니거나, 상어가 있다면
            if not (0 <= ni < 4 and 0 <= nj < 4) or (ni == ci and nj == cj):
                continue
            board[f_i][f_j][1] = nv
            # 물고기와 위치 바꾸기
            board[f_i][f_j], board[ni][nj] = board[ni][nj], board[f_i][f_j]
            break

    # 상어 이동
    sv = board[ci][cj][1] - 1
    for i in range(1, 5):
        ni = ci + di[sv] * i
        nj = cj + dj[sv] * i
        if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj][0] > 0:
            # 이전 정보가 남아있게 복사해서 넘겨준다.
            dfs(ni, nj, cnt, copy.deepcopy(board))


dfs(0, 0, 0, board)
print(ans)