N = int(input())

t = []
p = []
save = []
for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    # 기본값으로 페이를 넣어준다.
    save.append(b)

# 인덱스 에러 방지
save.append(0)

for n in range(N-1, -1, -1):
    # 범위를 벗어나면 그 전값을 넣어준다.
    if t[n] + n > N:
        save[n] = save[n+1]
    # 범위 안이라면 최대값 갱신
    else:
        save[n] = max(save[n+1], p[n] + save[n + t[n]])

print(save[0])