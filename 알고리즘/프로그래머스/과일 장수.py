# 한 상자에는 사과를 m개 담을 수 있다. (남는 사과는 버림)
# 사과 상자의 가격은 m * (가장낮은 점수)
# 가장 많이 팔았을 때의 최대 이익

# 가장 높은 가격 순서대로 상자에 담아 판다. => sort
# k개 씩 끊어서 담으면 answer에 값을 더해준다.

# def solution(k, m, score):
#     answer = 0
#     # 내림차순 정렬
#

#     while len(score) >= m:
#         answer += min(score[:m]) * m
#         score = score[m:]

#     return answer

def solution(k, m, score):
    answer = 0

    # 사과의 갯수를 count에 저장
    count = [0] * 10
    for i in range(len(score)):
        count[score[i]] += 1

    # 상자가 만들어 질 수 있는 갯수
    time = len(score) // m

    idx = k
    for _ in range(time):
        cnt = 0
        while idx > 0:
            # 해당 갯수가 현재 필요한 갯수보다 크다면 답에 현재 이익을 더하고 count에서 갯수를 빼준다.
            if count[idx] >= m - cnt:
                answer += idx * m
                count[idx] -= m - cnt
                break
            # 부족하면 cnt에 현재 갯수를 저장하고 다음 점수의 사과에서 부족한 갯수를 충당한다.
            else:
                cnt += count[idx]
                idx -= 1

    return answer