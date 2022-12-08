from collections import deque

# 수빈이의 위치와 동생의 위치
N, K = map(int, input().split())
# 최소 거리와 방법의 갯수를 저장하는 변수
cnt = 0
# 방문 타임, 횟수
visit = [[-1, 0]for _ in range(100001)]


def bfs():
    global cnt
    que = deque()
    que.append(N)
    visit[N][0] = 0
    visit[N][1] = 1
    while que:
        now = que.popleft()

        for i in [now + 1, now - 1, now * 2]:
            if 0 <= i <= 100000:
                # 처음 방문이라면 걸린시간과 경우의 수를 갱신한다.
                if visit[i][0] == -1:
                    que.append(i)
                    visit[i][0] = visit[now][0] + 1
                    visit[i][1] = visit[now][1]

                # 처음으로 도착하지 않았지만 최단거리라면 갯수를 갱신한다.
                elif visit[i][0] == visit[now][0] + 1:
                    visit[i][1] += visit[now][1]



bfs()
print(visit[K][0])
print(visit[K][1])