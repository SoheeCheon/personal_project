N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 오름차순으로 출력
numbers.sort()


def permutation(lst, n):
    if len(lst) == M:
        for num in range(M):
            print(lst[num], end=' ')
        print()
        return

    # 정렬된 것을 깨지 않기 위해서 선택한 숫자보다 작은 값은 범위내에 포함하지 않음
    for i in range(n, N):
        if not numbers[i] in lst:
            lst.append(numbers[i])
            permutation(lst, i)
            lst.pop()

permutation([], 0)
