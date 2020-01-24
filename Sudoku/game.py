board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# Function that prints board
def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        for j in range(len(b)):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + ' ', end='')


# Function that finds empty space
def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == 0:
                return (i, j)  # row, col
    return -1, -1


def empty_locations(board):
    empty = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty.append((i,j))
    return empty


# Functions that check if the number can be placed in that location
def check_row(b, row, num):
    if num in b[row]:
        return False
    return True


def check_col(b, col, num):
    for i in range(len(b)):
        if b[i][col] == num:
            return False
    return True


def check_square(b, col, row, num):
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) == (row, col):
                return False
    return True


def check_location(b, row, col, num):

    row_safe = check_row(b, row, num)
    col_safe = check_col(b, col, num)
    square_safe = check_square(b, row - row % 3, col - col % 3, num)

    if row_safe and col_safe and square_safe:
        return True
    else:
        return False


# Function that recursively tries numbers recursively:
#   returns a number between 1 and 9 or -1 (if no number between 1-9 checks the constraints)
def try_number(board, row, col, num=1):
    if num == 0:
        num = 1
    if num > 9:
        return -1
    if check_row(board, row, num) and check_col(board, col, num) and check_square(board, row - row%3, col-col%3, num):
        return num
    else:
        num += 1
        return try_number(board, row, col, num)


# Function that solves the board using the back-tracking algorithm
def solve_board(board):
    empty_array = solve_single_space(board)
    backtracking(board, empty_array)
    print_board(board)

    return


# Function that solves the only
def solve_single_space(board):
    empty_array = empty_locations(board)
    change = False
    for row, col in empty_array:
        number_array = []
        number = 0
        while number < 10:
            number = try_number(board, row, col, number+1)
            if number == -1:
                break
            number_array.append(number)

        if len(number_array) == 1:
            board[row][col] = number_array[0]
            change = True

        if change:
            solve_single_space(board)

    return empty_array


# Function that uses the backtracking algorithm
def backtracking(board, solved_array=[], backFlag=False):
    if not backFlag:
        row, col = find_empty(board)
    else:
        row, col = solved_array[-1]
    if (row, col) == (-1, -1):
        return
    number = board[row][col]
    number = try_number(board, row, col, number)

    if number != -1:
        board[row][col] = number
        solved_array.append((row, col))
        backtracking(board, solved_array)
    else:
        solved_array.pop(-1)
        backtracking(board, solved_array, backFlag=True)








print('Original Board:')
print_board(board)
print('')
print('Solved Board:')
solve_board(board)