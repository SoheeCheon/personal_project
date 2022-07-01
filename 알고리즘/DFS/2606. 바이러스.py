# N: 컴퓨터의 갯수, M: 간선정보의 갯수
N = int(input())
M = int(input())

# 인덱스 조정을 위해서
arr = [[0] * (N+1) for _ in range(N+1)]

# 간선정보 불러들이기
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1


visited = [0] * (N+1)

ans = 0
def dfs(n):
    global ans

    visited[n] = 1

    for i in range(1, N+1):
        if not visited[i] and arr[n][i]:
            dfs(i)
            ans += 1

dfs(1)
# 1번 컴퓨터는 이미 감염되었으므로 제외
print(ans)

