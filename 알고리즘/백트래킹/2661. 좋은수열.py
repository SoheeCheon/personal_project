N = int(input())

ans = "3" * N

def check(check_word, string):
    next_word = check_word + string
    length = int(len(next_word))
    for i in range(1, int(length/2) +1):
        # 중복되는 수열이 하나라도 있으면 False
        if next_word[length-i:] == next_word[length- i*2:length-i]:
            return False
    return True

# 인접한 두 개의 부분 수열이 동일하면 나쁜 수열
def make_number(word):
    global ans
    idx = len(word)
    # 가지치기 조건
    if idx > 0 and int(ans[:idx]) < int(word):
        return

    if idx == N:
        ans = word
        return

    # 값은 1,2,3 밖에 들어가지 않음
    for i in range(1, 4):
        if len(word) == 0 or check(word, str(i)):
            make_number(word + str(i))


make_number("")
print(ans)