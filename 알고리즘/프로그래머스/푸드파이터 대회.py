# 선1 ----- 물 ------ 선2
# 물을 먼저먹는 사람이 승리
# 칼로리가 낮은 음식순으로 배치함
# 1. 두곳모두 배치해야되기에 짝수로 나눠지는 것만 사용가능
# 2. word배열을 1번부터 시작하여 넣는다.
# 3. word을 뒤집어서 합쳐 리턴한다.
def solution(food):
    answer = ''

    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    return answer + "0" + answer[::-1]