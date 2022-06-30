# N개의 단어, K개의 알파벳
N, M = map(int, input().split())

words = [set(input().rstrip()) for _ in range(N)]

learn = [0] * 26
ans = 0


def backtracking(idx, count, learn, words):
    global ans

    # 새로 배우는 알파벳이 M - 5개가 되면 현재있는 단어들을 읽어본다
    if count == M - 5:
        tmp = 0
        for word in words:
            isContain = True
            for w in word:
                # 단어중에 못 배운 알파벳이 포함되어 있다면 for문을 빠져나오고
                # 다음 단어를 시작한다.
                if not learn[ord(w) - ord('a')]:
                    isContain = False
                    break

            # 단어를 읽을 수 있으면 갯수를 하나씩 추가하고 답을 갱신한다.
            if isContain:
                tmp += 1
        ans = max(tmp, ans)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            backtracking(i, count + 1, learn, words)
            learn[i] = False


if M < 5:
    print(0)
elif M == 26:
    print(N)
else:
    # 이 5개는 필수적으로 배워야 하는 단어
    alpha = ['a', 'c', 'n', 't', 'i']
    for c in alpha:
        learn[ord(c) - ord('a')] = True

    backtracking(1, 0, learn, words)

    print(ans)
