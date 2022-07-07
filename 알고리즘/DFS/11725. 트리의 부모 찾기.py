import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())

# 노드의 트리는 무조건 1
# 해당 값을 기준으로 노드를 작성
tree = [[] for _ in range(N+1)]
lst = [0]*(N+1)

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

lst[1] = 99

def bfs():
    q = []
    q.append(1)

    while q:
        now = q.pop(0)
        for i in tree[now]:
            if lst[i] == 0:
                lst[i] = now
                q.append(i)


bfs()
for i in lst[2:]:
    print(i)