import pygame
import sys
from components import get_grid_position, check_winner, update_board, draw_grid, draw_board,reset_game

pygame.init()

background_color = (0, 0, 0)
running = True
window_size = 300
line_color = (0, 255,0)
line_width = 4
grid_size = 3
cell_size = window_size // grid_size

x_img = pygame.image.load('/home/dhruva/tictactoe/X.png')
o_img = pygame.image.load('/home/dhruva/tictactoe/O.png')
x_img = pygame.transform.scale(x_img, (cell_size, cell_size))
o_img = pygame.transform.scale(o_img, (cell_size, cell_size))

# Set up the display
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Tic Tac Toe')

# Game state variables
board = [['' for _ in range(grid_size)] for _ in range(grid_size)]
current_player = 'X'
winner = None


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
            mouse_x, mouse_y = event.pos
            row, col = get_grid_position(mouse_x, mouse_y, cell_size)
            if update_board(board, row, col, current_player):
                current_player = 'O' if current_player == 'X' else 'X'
                winner = check_winner(board)
                if winner:
                    print(f"Winner: {winner}")
        elif winner:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

    draw_grid()
    draw_board(board)
    screen.fill(background_color)
    pygame.display.flip()

pygame.quit()
sys.exit()
