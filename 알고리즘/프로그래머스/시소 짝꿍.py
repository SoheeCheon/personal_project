from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)

    for n in count.values():
        if n > 1:
            answer += n * (n - 1) / 2

    check = [1 / 2, 2 / 3, 3 / 4]
    weight = set(weights)
    for w in weight:
        for c in check:
            if w * c in weight:
                answer += (count[w] * count[w * c])

    return answer
