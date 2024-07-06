#Importing necessary modules
import pygame as pg



#Setting game constant and starting
pg.init()
WIDTH, HEIGHT = 800, 800
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Conway's game of life")

BLACK = (0,0,0)
WHITE = (255,255,255)
BLOCK_SIZE = 20
GRID_COLOR = "#3c3c3b"
GRID_SIZE = 40

#Loading images
icon_img = pg.image.load('imgs/planet-earth.png')
pg.display.set_icon(icon_img)

#Drawing grid
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pg.draw.line(win,GRID_COLOR, (x,0), (x,HEIGHT))
        for y in range(0, HEIGHT, BLOCK_SIZE):
            pg.draw.line(win, GRID_COLOR, (0,y), (WIDTH, y))
class Cell:
    def __init__(self):
        self.clicked = 0
board = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

#Zwraca  ilość żywych sąsiadów
def count_neighbors(row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for first, second in directions:
        one, two = row + first, col + second
        if 0 <= one < GRID_SIZE and 0 <= two < GRID_SIZE and board[one][two].clicked == 1:
            count += 1
    return count
#Zwraca nam uaktualnioną planszę
def update_board():
    new_board = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            neighbors = count_neighbors(row, col)
            if board[row][col].clicked == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[row][col].clicked = 0
                else:
                    new_board[row][col].clicked = 1
            else:
                if neighbors == 3:
                    new_board[row][col].clicked = 1
    return new_board



#main loop
def main():
    global board
    running = True
    edit_mode = True


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    row = event.pos[1] // BLOCK_SIZE
                    col = event.pos[0] // BLOCK_SIZE
                    if board[row][col].clicked == 0:
                        board[row][col].clicked = 1
                    elif board[row][col].clicked == 1:
                        board[row][col].clicked = 0
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    edit_mode = not edit_mode

        win.fill(BLACK)


        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                color = WHITE if cell.clicked == 1 else BLACK
                pg.draw.rect(win, color, (x*BLOCK_SIZE, y*BLOCK_SIZE, 20, 20))
        draw_grid()
        pg.display.update()

        if not edit_mode:
            board = update_board()

    pg.quit()


if __name__ == "__main__":
    main()