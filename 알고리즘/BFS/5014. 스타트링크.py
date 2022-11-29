from collections import deque

F, S, G, U, D = map(int, input().split())
# 무한 while을 중지하기 위한 visit
visit = [0] * (F+1)

def bfs():
    que = deque([])
    # 큐에 현재 위치와 횟수를 저장한다
    que.append((S, 0))
    while que:
        now, cnt = que.popleft()
        # 위치에 도착했을 때 횟수를 출력
        if now == G:
            print(cnt)
            return

        # 위로 올라가는 범위는 최대 F층 까지
        if now + U <= F and visit[now + U] == 0:
            que.append((now+U, cnt+1))
            visit[now+U] = 1

        # 아래로 내려가는 범위는 최대 1층
        if now - D >= 1 and visit[now-D] == 0:
            que.append((now-D, cnt+1))
            visit[now-D] = 1

    # 도착할 수 없다면 메세지를 출력
    print("use the stairs")
    return


bfs()