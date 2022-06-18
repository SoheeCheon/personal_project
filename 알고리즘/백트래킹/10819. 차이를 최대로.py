N = int(input())
lst = list(map(int, input().split()))

ans = 0
result = []


def permutation(lst):
    if len(lst) == N:
        result.append(lst[:])
        return

    for i in range(N):
        if not i in lst:
            lst.append(i)
            permutation(lst)
            lst.pop()


permutation([])

for ele in result:
    ssum = 0
    for num in range(N-1):
        ssum += abs(lst[ele[num]] - lst[ele[num+1]])

    ans = max(ans, ssum)

print(ans)
