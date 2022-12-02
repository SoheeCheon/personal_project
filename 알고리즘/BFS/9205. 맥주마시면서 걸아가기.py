from collections import deque

def bfs():
    global con_cnt
    que = deque()
    que.append((home[0], home[1]))
    visit = [0]*con_cnt
    while que:
        cx, cy = que.popleft()
        # 페스티벌에 도착한다면 happy 출력
        if abs(cx - festival[0]) + abs(cy - festival[1]) <= 1000:
            print('happy')
            return
        for i in range(con_cnt):
            if visit[i] == 0:
                nx, ny = convience[i][0], convience[i][1]
                if abs(cx - nx) + abs(cy - ny) <= 1000:
                    que.append((nx, ny))
                    visit[i] = 1

    print("sad")
    return


T = int(input())
for _ in range(T):
    con_cnt = int(input())
    home = list(map(int, input().split()))
    convience = []

    for _ in range(con_cnt):
        x, y = map(int, input().split())
        convience.append([x, y])

    festival = list(map(int, input().split()))
    bfs()

