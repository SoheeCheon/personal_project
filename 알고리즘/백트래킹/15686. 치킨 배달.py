from itertools import combinations

# 리스트의 크기 N, 최대의 치킨집의 갯수 M
N, M = map(int, input().split())
# 지도의 정보 1: 집, 2: 치킨집
arr = [list(map(int, input().split())) for _ in range(N)]

# 치킨집과 집의 위치 정보
chicken = []
house = []
# 행, 열 값이 들어감
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

# 치킨집의 조합
# 사용시 시간초과가 발생하여 모듈을 사용함
result = []
def my_combination(lst, n):
    if len(lst) == M:
        result.append(lst[:])

    for i in range(n, len(chicken)):
        if not i in lst:
            lst.append(i)
            my_combination(lst, n+1)
            lst.pop()


# 최소의 거리를 구해야함
ans = 99999
for chi in combinations(chicken, M):
    ssum = 0
    for h in house:
        # 백트래킹 조건
        if ans < ssum:
            break
        value = 999
        for m in range(M):
            value = min(value, abs(h[0] - chi[m][0]) + abs(h[1] - chi[m][1]))
        ssum += value

    ans = min(ssum, ans)

print(ans)