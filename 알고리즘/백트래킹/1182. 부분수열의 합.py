N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
if sum(lst) == S:
    cnt += 1

result = set()


def find(sset):
    global cnt, result
    if sset and sum(sset) == S:
        if not sset in result:
            result.add(tuple(sset))
            cnt += 1

    if len(sset) == N-1:
        return

    for ele in lst:
        if not ele in sset:
            sset.add(ele)
            find(sset)
            sset.remove(ele)


my_set = set()
find(my_set)

print(cnt)