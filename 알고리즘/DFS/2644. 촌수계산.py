import sys
sys.setrecursionlimit(10 ** 9)

#전체 사람
n = int(input())
# 촌수를 계산해야되는 2사람
a, b = map(int, input().split())

tree = [[] for _ in range(n+1)]

m = int(input())

for _ in range(m):
    # x 부모 / y 자손
    x, y = map(int , input().split())

    tree[y].append(x)
    tree[x].append(y)

check = [0] * (n+1)

def bfs(node):
    q = []
    q.append(node)
    while q:
        now = q.pop(0)
        for num in tree[now]:
            if check[num] == 0:
                check[num] = check[now] + 1
                q.append(num)

bfs(a)
print(check[b] if check[b] > 0 else -1)

