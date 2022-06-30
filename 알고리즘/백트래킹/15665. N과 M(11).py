N, M = map(int, input().split())
numbers = list(map(int, input().split()))
idx = [0] * N

# 오름차순으로 출력
numbers.sort()


def permutation(lst):
    if len(lst) == M:
        print(*lst)
        return

    overlap = 0
    for i in range(N):
        # if A in B 문으로 중복을 검사하려 했으나 값이 커질수록 연산량도 많아져 시간초과 발생
        if overlap != numbers[i]:
            lst.append(numbers[i])
            overlap = numbers[i]
            permutation(lst)
            lst.pop()


permutation([])