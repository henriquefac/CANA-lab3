n = 8
board = [[0 for i in range(n)] for i in range(n)]

solutions = []

def check_column(board, row, column):
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False
    return True

def check_diagonal(board, row, column):
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, n, 1)):
        if board[i][j] == 1:
            return False
    return True

def nqn(board, row):
    if row == n:
        
        solutions.append([row[:] for row in board])
        return
    
    for i in range(n):
        if check_column(board, row, i) and check_diagonal(board, row, i):
            board[row][i] = 1
            nqn(board, row + 1)
            board[row][i] = 0

nqn(board, 0)


for solution in solutions:
    for row in solution:
        print(row)
    print("\n")
