def get_grid_position(mouse_x, mouse_y):
    row = mouse_y // 100
    col = mouse_x // 100
    return row, col

def update_board(board, row, col, player):
    if board[row][col] == '':
        board[row][col] = player
        return True
    return False