# 삼총사가 되는 경우의 수를 구한다.
# Combination을 활용하여 합이 0이 되는 경우를 찾는다.

from itertools import combinations


def solution(number):
    answer = 0
    for com in combinations(number, 3):
        if sum(com) == 0:
            answer += 1

    return answer