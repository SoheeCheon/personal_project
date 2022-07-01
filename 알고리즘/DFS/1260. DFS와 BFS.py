# 정점의 갯수, 간선의 갯수, 탐색을 시작할 번호
N, M, V = map(int, input().split())

# 인덱스 에러를 방지하기 위해서
# 2차원 리스트로 저장
lst = [[0] * (N+1) for _ in range(N + 1)]

# 간선정보를 1로 저장
for _ in range(M):
    s, e = map(int, input().split())
    lst[s][e] = lst[e][s] = 1


Dvisit = [0] * (N+1)

# dfs
def dfs(v):
    Dvisit[v] = 1
    # 방문한 순서대로 출력
    print(v, end=" ")
    # 갈수 있고 방문하지 않았다면 다음 번호로
    for i in range(1, N+1):
        if Dvisit[i] == 0 and lst[v][i] == 1:
            dfs(i)

dfs(V)
print()

Bque = [V]
Bvisited = [0] * (N + 1)
while Bque:
    # 갈 수 있는 방향을 모두 검사함
    now = Bque.pop(0)

    if not Bvisited[now]:
        Bvisited[now] = 1
        print(now, end=" ")

    for i in range(1, N+1):
        if not Bvisited[i] and lst[now][i]:
            Bque.append(i)



