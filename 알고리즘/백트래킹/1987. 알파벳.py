
R, C = map(int, input().split())
lst = [input() for _ in range(R)]

d = [(0,1), (0, -1), (1, 0), (-1, 0)]


def DFS(ci, cj, cnt):
    global ans
    # 최대 갯수는 바로바로 갱신
    ans = max(cnt, ans)

    for di, dj in d:
        ni = ci + di
        nj = cj + dj
        # 다음 인덱스가 범위 안에있고 알파벳이 단어에 포함이 되지 않는다면 다음으로 이동
        if 0 <= ni < R and 0 <= nj < C and not lst[ni][nj] in alpha:
            alpha.add(lst[ni][nj])
            DFS(ni, nj, cnt + 1)
            alpha.remove(lst[ni][nj])


ans = 0
alpha = set()
alpha.add(lst[0][0])
# 말은 좌측상단 고정
DFS(0, 0, 1)

print(ans)