import pygame
from network import Network
from game import Game

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
pygame.font.init()  
SquareFont = pygame.font.SysFont('Comic Sans MS', 150)
ButtonFont = pygame.font.SysFont('Comic Sans MS', 35)
PlayerFont = pygame.font.SysFont('Comic Sans MS', 30)
FPS = 60
squareHeight,squareWidth = 200,200


n = Network()
p = n.getP()
def main():
    global game
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        game = n.send("get")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                checkMouseClick()
        draw_window()
        draw_all()
        update_display()
    
    pygame.quit()

def draw_all():
    draw_reset_button()
    draw_board()
    draw_player()
    if not game.ready:
        draw_waiting_for_opponent()
    if(game.Winner == 0 and game.WhoseTurn == int(p) and game.ready):
        hover_squares()
    if(game.Winner != 0):
        draw_winner_banner()
    update_display()

def draw_main_menu():
    pass

def draw_waiting_for_opponent():
    xLoc = 400
    yLoc = 400
    pygame.draw.rect(WINDOW, WHITE, [xLoc-200,yLoc - 125, 400,100])
    pygame.draw.rect(WINDOW, BLACK, [xLoc-202,yLoc - 127, 400,100],4)
    valueSurface = ButtonFont.render("Waiting For Opponent", True, BLACK)
    WINDOW.blit(valueSurface,(xLoc-175 ,yLoc - 100))
    

def hover_squares():
    mouse = pygame.mouse.get_pos()
    for i, x in enumerate(game.board):
        for j, y in enumerate(x):
            xLoc = (100 + (squareWidth * i))
            yLoc = (100 + (squareHeight * j))
            if xLoc <= mouse[0] <= (xLoc + squareWidth) and yLoc <= mouse[1] <= (yLoc + squareHeight):
                if game.WhoseTurn == -1:
                    valueSurface = SquareFont.render("X", True, RED)
                    valueSurface.set_alpha(75)
                if game.WhoseTurn == 1:
                    valueSurface = SquareFont.render("O", True, BLUE)
                    valueSurface.set_alpha(75)
                if game.board[j][i] == 0: 
                    WINDOW.blit(valueSurface,(xLoc + squareWidth/5 ,yLoc + squareHeight/256))

    
def draw_winner_banner():
    xLoc = 400
    yLoc = 400
    pygame.draw.rect(WINDOW, WHITE, [xLoc-150,yLoc - 125, 300,100])
    pygame.draw.rect(WINDOW, BLACK, [xLoc-152,yLoc - 127, 300,100],4)
    if int(p) == game.Winner:
        valueSurface = ButtonFont.render("You Win", True, BLACK)
    elif int(p) == game.Winner * -1:
        valueSurface = ButtonFont.render("You Lose", True, BLACK)
    if game.Winner == 2:
        valueSurface = ButtonFont.render("A DRAW!", True, BLACK)
    WINDOW.blit(valueSurface,(xLoc-75 ,yLoc - 100))

def draw_window():
    WINDOW.fill(BEIGE)

def update_display():
    pygame.display.update()
    
def draw_board():
    for i, x in enumerate(game.board):
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

def checkMouseClick():
    global game
    if(game.ready):
        mouse = pygame.mouse.get_pos()
        ResetXLoc = 400
        ResetYLoc = 50
        if ResetXLoc - 100 <= mouse[0] <= (ResetXLoc+100) and ResetYLoc -25 <= mouse[1] <= (ResetYLoc +25):
            game = n.send("reset")
        if game.Winner == 0:
            if game.WhoseTurn == int(p):
                for i, x in enumerate(game.board):
                    for j, y in enumerate(x):
                        xLoc = (100 + (squareWidth * i))
                        yLoc = (100 + (squareHeight * j))
                        if xLoc <= mouse[0] <= (xLoc + squareWidth) and yLoc <= mouse[1] <= (yLoc + squareHeight):
                            if game.board[j][i] == 0: 
                                game = n.send(str(j) + "," + str(i))
                                draw_all()

def draw_player():
    xLoc = 700
    yLoc = 50
    valueSurface = PlayerFont.render("You are: "  , True, BLACK)
    if int(p) == 1:
        playerSurface = PlayerFont.render("O"  , True, BLUE)
    else:
        playerSurface = PlayerFont.render("X" , True, RED)
    WINDOW.blit(valueSurface,(xLoc-75 ,yLoc - 50))
    WINDOW.blit(playerSurface,(xLoc + 50 ,yLoc - 50))

def draw_reset_button():
    xLoc = 400
    yLoc = 50
    pygame.draw.rect(WINDOW, BLACK, [xLoc-102,yLoc - 27, 203,53],2)
    pygame.draw.rect(WINDOW, GREY, [xLoc-100,yLoc - 25, 200,50])
    valueSurface = ButtonFont.render("Reset", True, BLACK)
    WINDOW.blit(valueSurface,(xLoc-50 ,yLoc - 25))

if __name__ == "__main__":
    main()