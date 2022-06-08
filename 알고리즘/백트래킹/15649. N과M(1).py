N, M = map(int, input().split())


def permutation(lst, n):
    if n == M:
        for i in range(M):
            print(f'{lst[i]}', end=' ')
        print('')
        return

    for i in range(1, N+1):
        if not i in lst:
            lst.append(i)
            permutation(lst, n+1)
            lst.pop()


permutation([], 0)