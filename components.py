import pygame


window_size = 300
screen = pygame.display.set_mode((window_size, window_size))
line_width = 2
grid_size = 3
cell_size = window_size // grid_size

x_img = pygame.image.load('/home/dhruva/tictactoe/X.png')
o_img = pygame.image.load('/home/dhruva/tictactoe/O.png')
x_img = pygame.transform.scale(x_img, (100, 100))
o_img = pygame.transform.scale(o_img, (100, 100))

def get_grid_position(mouse_x, mouse_y,cell_size):
    row = mouse_y // cell_size
    col = mouse_x // cell_size
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
def draw_grid():
    """Draw the Tic Tac Toe grid."""
    for i in range(1,cell_size):
        pygame.draw.line(screen, (0,0,0), (0, i * cell_size), (window_size, i * cell_size), line_width)
        pygame.draw.line(screen, (0,0,0), (i * cell_size, 0), (i * cell_size, window_size), line_width)

def draw_board(board):
    """Draw the X's and O's on the board."""
    for row in range(grid_size):
        for col in range(grid_size):
            if board[row][col] == 'X':
                screen.blit(x_img, (col * cell_size, row * cell_size))
            elif board[row][col] == 'O':
                screen.blit(o_img, (col * cell_size, row * cell_size))


def reset_game():
    global board, current_player, winner
    board = [['' for _ in range(grid_size)] for _ in range(grid_size)]
    current_player = 'X'
    winner = None
                