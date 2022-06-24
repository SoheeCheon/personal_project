arr = [input() for _ in range(9)]
sudoku = [[0] * 9 for _ in range(9)]

# str 에서 list 로 변환
for i in range(9):
    for j in range(9):
        sudoku[i][j] = int(arr[i][j])

# 빈공간 확인
def find_empty():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    # 빈공간이 없을떄
    return None, None

# 유효한 값 확인
def vaild(col, row, num):
    # 가로/ 세로 확인
    for i in range(9):
        if sudoku[col][i] == num:
            return False

        elif sudoku[i][row] == num:
            return False

    # 3 * 3 박스 확인
    box_col = col // 3 * 3
    box_row = row // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[box_col + i][box_row + j] == num:
                return False

    return True


def check():
    global sudoku
    col, row = find_empty()

    # 빈공간이 없으면 빠져나감
    if col is None:
        return True

    for i in range(1, 10):
        # 값이 유효한지 확인
        if vaild(col, row, i):
            sudoku[col][row] = i
            if check():
                return True
            sudoku[col][row] = 0

    return False


check()

for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end="")
    print('')


