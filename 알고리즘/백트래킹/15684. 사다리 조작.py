N, M, H = map(int, input().split())
# 연결선이 위치하는 곳
# a : 높이, b : 세로선 위치
bridge = [list((map(int, input().split()))) for _ in range(M)]

radder = [[0] * N for _ in range(H)]

# 연결 정보를 추가
for a, b in bridge:
    radder[a][b] = 1
    radder[a][b+1] = 1


def check()
