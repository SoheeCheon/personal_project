T = int(input())

for _ in range(T):
    vps = input()

    # 여는 괄호 갯수를 카운팅
    open = 0
    stop = False
    for str in vps:
        # 처음에 여는 괄호가 나오면 vps가 성립이 되지 않으므로 제거
        if open == 0 and str == ")":
            stop = True
            break

        if str == "(":
            open += 1
        else:
            open -= 1

    if stop:
        print("NO")
    elif open == 0:
        print("YES")
    else:
        print("NO")
