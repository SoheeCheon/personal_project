# 1 ~ 49 까지 고른다
lst = [list(map(int, input().split()))]
# 0이 들어올때까지 입력받는다.
while not 0 in lst[-1]:
    input_lst = list(map(int, input().split()))
    lst.append(input_lst)


def permutation(cnt, idx):
    if cnt == 6:
        for j in range(6):
            print(combi[j], end=" ")
        print()
        return

    for i in range(idx, len(lotto)):
        combi[cnt] = lotto[i]
        permutation(cnt+1, i+1)


combi = [0] * 6
for i in range(len(lst) - 1):
    cnt = lst[i][0]
    lotto = lst[i][1:]

    permutation(0, 0)
    print()


