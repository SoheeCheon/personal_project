N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 9999999999999
def search(start, next, ssum, visited):
    global ans
    # 탈출 조건
    if ans < ssum:
        return

    # 갱신조건
    if len(visited) == N:
        if arr[next][start] != 0:
            ans = min(ans, ssum + arr[next][start])
        return

    # 아직 다녀오지 않고 같은 지역이 아니며 처음 출발한 곳이 아니면
    for i in range(N):
        if arr[next][i] != 0 and i not in visited:
            visited.append(i)
            search(start, i, ssum + arr[next][i], visited)
            visited.pop()


for i in range(N):
    search(i, i, 0, [i])

print(ans)