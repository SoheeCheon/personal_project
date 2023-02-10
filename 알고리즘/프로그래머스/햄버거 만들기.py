# 연속으로 '야채 고기 빵'이 나와야한다
def solution(ingredient):
    answer = 0
    idx = 0
    while idx < len(ingredient) - 2:
        if ingredient[idx: idx+4] == [1,2,3,1]:
            # 빵 - 야채 - 고기 - 빵 순은 리스트에서 제거하고 idx를 재정립한다.
            del(ingredient[idx:idx+4])
            # 현재 위치에서 한칸 전으로 가기위해 -2 = -3 + 1
            idx -= 3
            answer += 1
        idx += 1
    return answer