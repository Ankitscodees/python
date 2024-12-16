import pygame
import sys

def maze_escape():
    pygame.init()

    # Screen and grid settings
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Maze Escape")
    clock = pygame.time.Clock()
    cell_size = 40
    grid = [
        "##########",
        "#        #",
        "#  ####  #",
        "#  #     #",
        "#  #######",
        "#        #",
        "######## #",
        "#        #",
        "##########"
    ]

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)

    # Player settings
    player_pos = [1, 1]

    def draw_grid():
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                color = black if cell == "#" else white
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, green, (player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, red, ((8 * cell_size), (7 * cell_size), cell_size, cell_size))

    print("Navigate the player (green) to the red square to win!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x, y = player_pos
                if event.key == pygame.K_UP and grid[y - 1][x] == " ":
                    player_pos[1] -= 1
                if event.key == pygame.K_DOWN and grid[y + 1][x] == " ":
                    player_pos[1] += 1
                if event.key == pygame.K_LEFT and grid[y][x - 1] == " ":
                    player_pos[0] -= 1
                if event.key == pygame.K_RIGHT and grid[y][x + 1] == " ":
                    player_pos[0] += 1

        if player_pos == [8, 7]:
            print("You escaped the maze! Well done!")
            pygame.quit()
            sys.exit()

        screen.fill(black)
        draw_grid()
        pygame.display.flip()
        clock.tick(30)

maze_escape()
