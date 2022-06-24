# 부등호의 갯수
k = int(input())

arr = list(input().split())

# 최댓값과 최솟값
min_ans = ''
max_ans = ''
visited = [0] * 10

# 부등호 체크
def check(num1, num2, oppe):
    if oppe == "<":
        return num1 < num2
    else:
        return num1 > num2


def solve(idx, s):
    global min_ans, max_ans

    if idx == k + 1:
        if len(min_ans) == 0:
            min_ans = s
        # 최대값은 계속 갱신되어 끝값이 들어감
        else:
            max_ans = s
        return

    # 반복문을 돌면서 작은 값부터 들어가기 때문에 min 이후 max를 넣을 수 있다.
    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(s[-1], str(i), arr[idx-1]):
                visited[i] = 1
                solve(idx + 1, s + str(i))
                visited[i] = 0


solve(0, "")
print(max_ans)
print(min_ans)