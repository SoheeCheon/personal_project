N, M = map(int, input().split())
number = list(map(int, input().split()))

number.sort()


def combination(lst):
    if len(lst) == M:
        for j in range(M):
            print(lst[j], end=' ')
        print('')
        return

    for i in range(N):
        if not number[i] in lst:
            lst.append(number[i])
            combination(lst)
            lst.pop()


combination([])