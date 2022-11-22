N, M = map(int, input().split())

miro = [[0] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]

for n in range(N):
    line = input()
    for m in range(M):
        miro[n][m] = int(line[m])


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs():
    que = [(0, 0)]
    visit[0][0] = 1
    while que:
        i, j = que.pop(0)

        if i == (N-1) and j == (M-1):
            return
        for idx in range(4):
           ni = i + di[idx]
           nj = j + dj[idx]
           if 0 <= ni < N and 0 <= nj < M and miro[ni][nj] and not visit[ni][nj]:
               que.append((ni,nj))
               visit[ni][nj] = visit[i][j] + 1


bfs()
print(visit[N-1][M-1])

