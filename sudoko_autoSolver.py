import json
import random

#impot a random ssudoko problem form the JSON file.
load_boards = json.load(open("board.json", "r"))
main_board = load_boards[str(random.randint(0, len(load_boards)-1))]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Condition 1: number must be unique in the row.
def check_row(board: list[list[int]], row: int, value: int) -> bool:
    if value in board[row]: return False
    return True

# Condition 2: number must be unique in the col.
def check_col(board: list[list[int]], col: int, value: int) -> bool:
    for row in board:
        if row[col] == value: return False
    return True

# Condition 3: number must be unique in the 3x3 box.
def check_box(board: list[list[int]], row: int, col: int, value: int) -> bool:
    # calculate the box position.
    box_x = row // 3
    box_y = col // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == value: return False
    return True

def isValid_value(board: list[list[int]], row: int, col: int, value: int) -> bool:
    return check_row(board, row, value) and \
            check_col(board, col, value) and \
            check_box(board, row, col, value)

def find_emptyBox(board) -> tuple | bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: return row, col
    return False

def auto_solve() -> bool:
    box = find_emptyBox(main_board)
    if not box:
        return True
    row, col = box

    for value in range(1, 10):
        if isValid_value(main_board, row, col, value):
            main_board[row][col] = value
            if auto_solve():
                return True
            main_board[row][col] = 0
    return False

if __name__ == "__main__":
    auto_solve()
    print_board(main_board)