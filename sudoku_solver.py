sudoku = [
    [4, 0, 0, 0, 8, 0, 2, 9, 0],
    [0, 0, 1, 0, 0, 7, 0, 0, 0],
    [8, 0, 6, 0, 0, 0, 3, 0, 1],
    [0, 0, 4, 9, 1, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 7, 0, 4, 6, 1, 0],
    [0, 4, 8, 1, 3, 0, 5, 2, 6],
    [0, 3, 2, 0, 0, 6, 0, 0, 0],
    [0, 9, 5, 8, 7, 2, 1, 0, 4],
]

# sudoku = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]
'''
1. Pick empty square
2. Try all number until you find a working number
3. Repeat the process
4. If you find impossible position - backtrack 

'''


def solver(sudoku):
    find = find_empty_space(sudoku)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if solver(sudoku):
                return True

            sudoku[row][col] = 0

    return False


def valid(sudoku, num, pos):  # (pos = tuple with current position)
    # check the row
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False

    # check the col
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # check the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudoku[i][j] == num and (i, j) != pos:
                return False

    return True


def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(f" | ", end=" ")
            print(sudoku[i][j], end=" ")
        print()


def find_empty_space(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  # i = row, j = col
    return None


print_sudoku(sudoku)
solver(sudoku)

print()
print()

print_sudoku(sudoku)
