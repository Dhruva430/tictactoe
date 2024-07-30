import pygame
from components import get_grid_position,check_winner,update_board
pygame.init()

background_colour = (0, 0, 0)
(width, height) = (600, 400)
running = True


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Grid dimensions
grid_size = 300
cell_size = grid_size // 3
# Calculate starting position for centering the grid
start_x = (width - grid_size) // 2
start_y = (height - grid_size) // 2


line_color = (255, 0, 0)
line_width = 2
grid_lines = [
    # Horizontal lines
    (
        (start_x, start_y + cell_size),
        (start_x + grid_size, start_y + cell_size),
    ),  # First row
    (
        (start_x, start_y + 2 * cell_size),
        (start_x + grid_size, start_y + 2 * cell_size),
    ),  # Second row
    # Vertical lines
    (
        (start_x + cell_size, start_y),
        (start_x + cell_size, start_y + grid_size),
    ),  # First column
    (
        (start_x + 2 * cell_size, start_y),
        (start_x + 2 * cell_size, start_y + grid_size),
    ),  # Second column
]

board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
screen.fill(background_colour)

while running:
        # Draw grid lines
    for start_pos, end_pos in grid_lines:
        pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                row, col = get_grid_position(mouse_x, mouse_y)
                print(f"Grid position: ({row}, {col})")

                if update_board(board, row, col, current_player):
                    current_player = 'O' if current_player == 'X' else 'X'
                    winner = check_winner(board)
                    if winner:
                        print(f"Winner: {winner}")
                        running = False
    
    pygame.display.flip()
