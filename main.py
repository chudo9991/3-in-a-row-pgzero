import pgzrun
import random
import sys

mod = sys.modules['__main__']

N = 10
CELL = 32
WIDTH = CELL*N
HEIGHT = CELL*(N+2)
TITLE = "3-in-a-row"
FPS = 60

board = [[0 for i in range(N)] for j in range(N)]
clicks = 50

for i in range(N):
    for j in range(N):
        board[i][j] = mod.Actor("empty")
        board[i][j].sign = random.randint(0, 4)
        board[i][j].anchor = ("center", "center")
        board[i][j].left = CELL * j
        board[i][j].top = CELL * i
        if board[i][j].sign == 0:
            board[i][j].image = "13_bacon"
        elif board[i][j].sign == 1:
            board[i][j].image = "11_bun"
        elif board[i][j].sign == 2:
            board[i][j].image = "92_sandwich"
        elif board[i][j].sign == 3:
            board[i][j].image = "75_pudding"
        elif board[i][j].sign == 4:
            board[i][j].image = "81_pizza"
        else:
            board[i][j].image = "empty"
                 
def draw():                
    mod.screen.clear()
    mod.screen.draw.text("Clicks: " + str(clicks), center=(WIDTH/2, HEIGHT-32), color="white", fontsize=32)
    for i in range(N):
        for j in range(N):
            board[i][j].draw()

def on_mouse_down(button, pos):                
    global board, clicks
    clicks -= 10
    for i in range(N):
        for j in range(N):
            if board[i][j].collidepoint(pos) and button == mod.mouse.LEFT:
                board[i][j].top = i*CELL-5
                mod.animate(board[i][j], tween="bounce_end", duration=0.3, top=i*CELL)
                board[i][j].image = "empty"
                board[i][j].sign = 5
                

def update(dt):
    global board, clicks
    for i in range(N):
        for j in range(N):
            if board[i][j].sign == 5 and i != 0:
                    board[i][j].top = i*CELL-5
                    mod.animate(board[i][j], tween="bounce_end", duration=0.5, top=i*CELL)
                    board[i][j].image, board[i-1][j].image = board[i-1][j].image, board[i][j].image
                    board[i][j].sign, board[i-1][j].sign = board[i-1][j].sign, board[i][j].sign
                
            elif board[i][j].sign == 5 and i == 0:
                board[i][j].sign = random.randint(0, 4)                            
                if board[i][j].sign == 0:
                    board[i][j].image = "13_bacon"
                elif board[i][j].sign == 1:
                    board[i][j].image = "11_bun"
                elif board[i][j].sign == 2:
                    board[i][j].image = "92_sandwich"
                elif board[i][j].sign == 3:
                    board[i][j].image = "75_pudding"
                elif board[i][j].sign == 4:
                    board[i][j].image = "81_pizza"
                else:
                    board[i][j].image = "empty"

    for i in range(1,N-1):
        for j in range(1,N-1):        
                if (board[i][j].sign == board[i][j-1].sign and board[i][j].sign == board[i][j+1].sign): 
                    
                    board[i][j].top = i*CELL-5
                    mod.animate(board[i][j], tween="bounce_start", duration=0.1, top=i*CELL)
                    board[i][j].image = "empty"
                    board[i][j].sign = 5
                    
                    board[i][j-1].top = i*CELL-5
                    mod.animate(board[i][j-1], tween="bounce_start_end", duration=0.1, top=i*CELL)
                    board[i][j-1].image = "empty"
                    board[i][j-1].sign = 5

                    board[i][j+1].top = i*CELL-5
                    mod.animate(board[i][j+1], tween="bounce_end", duration=0.1, top=i*CELL)
                    board[i][j+1].image = "empty"
                    board[i][j+1].sign = 5

                    clicks += 3

pgzrun.go()