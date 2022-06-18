N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 차이가 최소가 되도록
def backtracking(cnt, idx):
    global ans
    if ans == 0:
        return

    if cnt == N/2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if lst[i] and lst[j]:
                    start += arr[i][j]
                elif not lst[i] and not lst[j]:
                    link += arr[i][j]

        ans = min(abs(start - link), ans)
        return

    for num in range(idx, N):
        if lst[num] == 0:
            lst[num] = 1

            backtracking(cnt + 1, idx+1)
            lst[num] = 0


ans = 99999
lst = [0] * N

backtracking(0, 0)

print(ans)