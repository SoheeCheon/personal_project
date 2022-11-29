from collections import deque

# 가로, 세로 정보
R, C = map(int, input().split())

# 고슴도치와 동굴의 위치
goal = []
hegihog = []
forest = []
for r in range(R):
    lst = list(input())
    for c in range(C):
        if lst[c] == 'D':
            goal = [r, c]
        elif lst[c] == 'S':
            hegihog = [r, c]

    forest.append(lst)

forest[hegihog[0]][hegihog[1]] == '.'

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs():
    que = deque([])
    que.append(hegihog)
    time = 0
    while que:
        cr, cc = que.popleft()
        if cr == goal[0] and cc == goal[1]:
            return time
        visit = [[0] * C for _ in range(R)]
        hegi_visit = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if forest[r][c] == "*" and visit[r][c] == 0:
                    for idx in range(4):
                        nr = r + dr[idx]
                        nc = c + dc[idx]
                        if not(0 <= nr < R and 0 <= nc < C):
                            continue
                        # 물이 차오르는 범위 표시
                        if forest[nr][nc] == "." and visit[nr][nc] == 0:
                            forest[nr][nc] = "*"
                            visit[nr][nc] = 1

        for idx in range(4):
            nr = cr + dr[idx]
            nc = cc + dc[idx]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if (forest[nr][nc] == '.' or forest[nr][nc] == 'D')and hegi_visit[nr][nc] == 0:
                que.append((nr, nc))

    return "KAKTUS"


print(bfs())

