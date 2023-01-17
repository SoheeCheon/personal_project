base = input()
compare = input()

N = len(base)
M = len(compare)

lst = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        # 단어가 같다면 값을 더해주고
        if base[i-1] == compare[j-1]:
            lst[i][j] = lst[i-1][j-1] + 1
        # 아니면 이전값으로 덮어씌운다.
        else:
            lst[i][j] = max(lst[i][j-1], lst[i-1][j])

print(lst[-1][-1])