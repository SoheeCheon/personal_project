from collections import deque

N, M = map(int, input().split())
# 수빈이가 방문할 곳의 시간을 체크하는 리스트
visit = [0] * 100001
# 자식 노드가 부모 노드를 알기 위한 리스트
check = [0] * 100001


def move(node):
    data = []
    temp = node
    for _ in range(visit[node]+1):
        data.append(temp)
        temp = check[temp]

    # 데이터를 역순으로 문자열의 형태로 출력한다.
    print(' '.join((map(str, data[::-1]))))


def bfs():
    que = deque([])
    # 현재 위치와 이동거리을 넣어둔다.
    que.append(N)
    while que:
        now = que.popleft()
        if now == M:
            print(visit[now])
            move(now)
            return

        # 수빈이가 이동할 수 있는 방향
        for next_node in (now-1, now+1, now*2):
            if 0 <= next_node <= 100000 and visit[next_node] == 0:
                visit[next_node] = visit[now] + 1
                que.append(next_node)
                # 지나온 위치를 표시하기 위해 현재 이동거리를 저장
                check[next_node] = now


bfs()