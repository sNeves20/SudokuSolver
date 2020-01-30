board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,0],
    [0,0,0,0,8,0,0,7,9]
]

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


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j   # Row, Column
    return -1, -1


def empty_locations(board):
    empty = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty.append((i, j))
    return empty


# Functions that check if the constraints are met
def check_row(board, row, num):
    if num in board[row]:
        return False
    return True


def check_col(board, col, num):
    for i in range(len(board)):
        if board[i][col] == num:
            return False
    return True


def check_square(board, row, col, num):
    box_x = col//3
    box_y = row//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != (row, col):
                return False
    return True


def constraint_check(board, row, col, num):

    if check_row(board, row, num) and check_col(board, col, num) and check_square(board, row, col, num):
        return True
    else:
        return False


#############################################################################################################

def try_number(board, row, col, num):
    if num == 0:
        num = 1
    if num > 9:
        return -1
    if constraint_check(board, row, col, num):
        return num
    else:
        num += 1
        return try_number(board, row, col, num)


# Function that solves the spaces where ony one number can be placed
def solve_singles(board):
    # Checking Empty positions
    empty_pos = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty_pos.append((i,j))

    # Checking which position has only one solution
    for row, col in empty_pos:
        sol = []
        num = 0
        while num != -1:
            num = try_number(board, row, col, num + 1)
            if num != -1:
                sol.append(num)

        if len(sol) == 1:
            board[row][col]=sol[0]
            solve_singles(board)

    return


def solve_board(board):
    empty_places = empty_locations(board)
    print("Empty locations: ", empty_places)
    print("Number of empty spaces: ", len(empty_places))
    empty_pointer = 0
    if not empty_places:
        print("This board is already solved after single space solve!")
        return
    solve = False
    while not solve:
        empty_pointer = backtracking(board, empty_places, empty_pointer)
        if empty_pointer == -99:
            print('This board can not be solved')
            return
        if empty_pointer == len(empty_places) - 1:
            print(empty_pointer)
            print(len(empty_places))
            solve = True
    print_board(board)
    return


def backtracking (board, empty_locations, empty_pointer):
    row, col = empty_locations[empty_pointer]
    number = board[row][col]
    if number == 9 and empty_pointer != 0:
        number = 0
    number = try_number(board, row, col, number + 1)
    if row == 0 and col == 5:
        print(number)
    if number == -1:
        if empty_pointer == 0:
            print("Board Could not be solved")
            exit(-99)
        print(empty_pointer)
        while number == -1:
            empty_pointer -= 1
            empty_pointer = backtracking(board, empty_locations, empty_pointer)
            number = try_number(board, row, col,  number+1)
        print(empty_pointer)
        board[row][col] = number
    else:
        board[row][col] = number

    return empty_pointer + 1


print('Initial Board:')
print_board(board)
#solve_singles(board)
print('')
print('Board After Single Solution Solve:')
print_board(board)
print('')
print("Board After Backtracking Algorithm:")
solve_board(board)
