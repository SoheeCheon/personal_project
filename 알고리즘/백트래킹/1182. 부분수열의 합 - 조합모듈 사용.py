N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
if sum(lst) == S:
    cnt += 1

result = []

def find(sset, n):
    global cnt, result
    if sset and sum(sset) == S:
        if not sset in result:
            result.append(sset)
            cnt += 1

    if len(sset) == N-1:
        return

    for ele in range(n, len(lst)):
        if not ele in sset:
            sset.add(ele)
            find(sset, n+1)
            sset.remove(ele)


my_set = set()
find(my_set, 0)

print(cnt)