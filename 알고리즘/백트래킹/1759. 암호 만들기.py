# L개의 알파벳으로 구성, 총 C개의 알파벳
L, C = map(int, input().split())
alpha = list(input().split())

alpha.sort()
moum = ['a', 'e', 'i', 'o', 'u']

def password(word, n):
    if len(word) == L:
        idx = 0
        cnt = 0
        Flag = False
        while idx < L:
            if word[idx] in moum:
                Flag = True
            else:
                cnt += 1
            idx += 1
        # 최소 요건 만족하는지 확인
        if cnt >= 2 and Flag:
            print(word)
        return

    for i in range(n, C):
        if not alpha[i] in word:
            word += alpha[i]
            password(word, i)
            word = word[:-1]


password('', 0)