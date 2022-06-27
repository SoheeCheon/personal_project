from itertools import combinations

N = int(input())

numbers = []
# 가능한 숫자가 0 ~ 9, 10가지 이므로 총 10개의 조합을 찾는다
for i in range(1, 11):
    # 1 ~ 10개의 조합을 실시
    # 작은 숫자부터 차례대로 들어오게 됨
    for comb in combinations(range(0, 10), i):
        # 리스트 형태로 바꿈
        comb = list(comb)
        # 내림차순으로 정렬
        # a > b : 이런형태를 만들기 위해서 정렬
        comb.sort(reverse=True)
        numbers.append(int("".join(map(str, comb))))

# 오름차순으로 정렬
numbers.sort()

try:
    print(numbers[N])
except:
    print(-1)
