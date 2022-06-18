N = int(input())


def permutation(lst, n):
    if n == N:
        for ele in lst:
            print(ele, end=" ")
        print('')
        return


    for i in range(1, N+1):
        if not i in lst:
            lst.append(i)
            permutation(lst, n+1)
            lst.pop()


permutation([], 0)

