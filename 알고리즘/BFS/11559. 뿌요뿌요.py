from collections import deque
import copy

# 6 * 12의 판
puyo = [list(input()) for _ in range(12)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def down():
    for x in range(6):
        for y in range(11, -1, -1):
            # 빈칸이라면
            if puyo[y][x] == '.':
                cnt = 0
                now_y = y
                while now_y > 0:
                    if puyo[now_y][x] == '.':
                        cnt += 1
                        now_y -= 1
                    else:
                        break

                if now_y == 0:
                    break

                # 위치를 바꿔준다.
                puyo[now_y][x], puyo[y][x] = puyo[y][x], puyo[now_y][x]



def bfs(x, y):
    global puyo
    que = deque()
    que.append((x, y))
    copypuyo = copy.deepcopy(puyo)
    copypuyo[x][y] ='.'
    cnt = 1
    while que:
        cx, cy = que.popleft()

        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            # 범위 안이고 같은 색깔이면서 방문하지 않았다면
            if 0 <= nx < 12 and 0 <= ny < 6 and copypuyo[nx][ny] == puyo[x][y] and copypuyo[nx][ny] != '.':
                cnt += 1
                que.append((nx, ny))
                copypuyo[nx][ny] = '.'


    # 4개 이상 연쇄 되었을 경우 삭제하고 리턴한다.
    if cnt >= 4:
        puyo = copypuyo
        return 1

    return 0


result = 0
while True:
    Flag = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                Flag += bfs(i, j)

    # 연쇄되어 삭제되는 것이 있다면 중력에 의해 떨어트리고
    if Flag:
        down()
        result += 1

    # 연쇄되어 삭제된게 없다면 연쇄수를 출력한다.
    else:
        print(result)
        break