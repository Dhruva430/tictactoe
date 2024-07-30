def get_grid_position(mouse_x, mouse_y):
    row = mouse_y // 100
    col = mouse_x // 100
    return row, col

def update_board(board, row, col, player):
    if board[row][col] == '':
        board[row][col] = player
        return True
    return False

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    
    # Check for draw
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        return 'Draw'
    
    return None