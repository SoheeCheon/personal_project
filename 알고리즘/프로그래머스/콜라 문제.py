# 총 몇 병을 가져갈 수 있나
# 받은 갯수를 // a 하여 몫을 더한다.

def solution(a, b, n):
    answer = 0
    # 현재 갯수가 더 이상 나눌 수 없을 때 까지 반복한다.
    while n >= a:
        bottle = (n // a) * b
        answer += bottle
        n = bottle + n % a

    return answer