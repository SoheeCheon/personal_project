from collections import deque

T = int(input())

for _ in range(T):
    I = int(input())

    chess = [[0] * I for _ in range(I)]

    start = tuple(map(int, input().split()))
    endi, endj = map(int, input().split())

    que = deque([])
    que.append(start)
    # 나이트가 이동하는 범위
    delta = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]


    def bfs():
        while que:
            ci, cj = que.popleft()
            if ci == endi and cj == endj:
                print(chess[ci][cj])
                return

            for idx in range(8):
                ni = ci + delta[idx][0]
                nj = cj + delta[idx][1]

                if 0 <= ni < I and 0 <= nj < I and chess[ni][nj] == 0:
                    que.append((ni, nj))
                    chess[ni][nj] = chess[ci][cj] + 1

    bfs()