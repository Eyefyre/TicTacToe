import pygame

WIDTH,HEIGHT = 800,800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (255,240,240)
BEIGE = (249,243,221)
RED = (255,0,0)
BLUE = (0,0,255)
cols,rows = 3,3
squares = [[0 for i in range(cols)] for j in range(rows)]
pygame.font.init()  
SquareFont = pygame.font.SysFont('Comic Sans MS', 150)
ButtonFont = pygame.font.SysFont('Comic Sans MS', 35)
FPS = 60
squareHeight,squareWidth = 200,200
WhoseTurn = 1
Winner = 0


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                checkMouseClick()

        draw_all()
    
    pygame.quit()

def draw_all():
    draw_window()
    draw_reset_button()
    draw_board()
    if(Winner != 0):
        draw_winner_banner()
    update_display()
    

def draw_winner_banner():
    global Winner
    xLoc = 400
    yLoc = 400
    pygame.draw.rect(WINDOW, WHITE, [xLoc-150,yLoc - 125, 300,100])
    pygame.draw.rect(WINDOW, BLACK, [xLoc-152,yLoc - 127, 300,100],4)
    if Winner == -1:
        valueSurface = ButtonFont.render("X WINS!", True, BLACK)
    if Winner == 1:
        valueSurface = ButtonFont.render("O WINS!", True, BLACK)
    if Winner == 2:
        valueSurface = ButtonFont.render("A DRAW!", True, BLACK)
    WINDOW.blit(valueSurface,(xLoc-75 ,yLoc - 100))

def printGrid():
    for x in squares:
        for y in x:
            print(y,end = " ")
        print()
    print()

def draw_window():
    WINDOW.fill(BEIGE)

def update_display():
    pygame.display.update()
    
def draw_board():
    for i, x in enumerate(squares):
        for j, y in enumerate(x):
            xLoc = (100 + (squareWidth * j))
            yLoc = (100 + (squareHeight * i))
            pygame.draw.rect(WINDOW, BLACK, [xLoc,yLoc, squareHeight,squareWidth], 4)
            pygame.draw.rect(WINDOW, GREY, [xLoc + 1,yLoc + 1, squareHeight-1,squareWidth-1])
            if y == -1:
                valueSurface = SquareFont.render("X", True, RED)
            if y == 1:
                valueSurface = SquareFont.render("O", True, BLUE)
            if(y != 0):
                WINDOW.blit(valueSurface,(xLoc + squareWidth/5 ,yLoc + squareHeight/256))

def checkWinCondition():
    DiagSum = 0
    for x in range(cols):
        sum = 0
        for y in range(rows):
            sum += squares[x][y]
            if(sum == 3):
                return 1
            if(sum == -3):
                return -1
    for x in range(cols):
        sum = 0
        for y in range(rows):
            sum += squares[y][x]
            if(sum == 3):
                return 1
            if(sum == -3):
                return -1
    for x in range(cols):
        for y in range(rows):
            if x == y:
                DiagSum += squares[x][y]
            if(DiagSum == 3):
                return 1
            if(DiagSum == -3):
                return -1
    DiagSum = 0
    for x in range(cols):
        for y in range(rows):
            if x + y == 2:
                DiagSum += squares[x][y]
            if(DiagSum == 3):
                return 1
            if(DiagSum == -3):
                return -1
    Draw = True
    for x in range(cols):
        for y in range(rows):
            if(squares[x][y] == 0):
                Draw = False
    if(Draw):
        return 2
    return 0


def checkMouseClick():
    global WhoseTurn
    global squares
    global Winner
    mouse = pygame.mouse.get_pos()
    ResetXLoc = 400
    ResetYLoc = 50
    if ResetXLoc - 100 <= mouse[0] <= (ResetXLoc+100) and ResetYLoc -25 <= mouse[1] <= (ResetYLoc +25):
        squares = [[0 for i in range(cols)] for j in range(rows)]
        Winner = 0
        #printGrid()
    if Winner == 0:
        for i, x in enumerate(squares):
            for j, y in enumerate(x):
                xLoc = (100 + (squareWidth * i))
                yLoc = (100 + (squareHeight * j))
                if xLoc <= mouse[0] <= (xLoc + squareWidth) and yLoc <= mouse[1] <= (yLoc + squareHeight):
                    if squares[j][i] == 0: 
                        squares[j][i] = WhoseTurn 
                        WhoseTurn = WhoseTurn * -1
                        Winner = checkWinCondition()
                    #printGrid()


def draw_reset_button():
    xLoc = 400
    yLoc = 50
    pygame.draw.rect(WINDOW, BLACK, [xLoc-102,yLoc - 27, 203,53],2)
    pygame.draw.rect(WINDOW, GREY, [xLoc-100,yLoc - 25, 200,50])
    valueSurface = ButtonFont.render("Reset", True, BLACK)
    WINDOW.blit(valueSurface,(xLoc-50 ,yLoc - 25))

if __name__ == "__main__":
    main()