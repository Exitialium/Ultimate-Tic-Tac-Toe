import pygame
import numpy as np
from tictactoe import GameModel
from grid import Grid



running = True;

game = GameModel()
surface = pygame.display.set_mode((500,500))
pygame.display.set_caption("Ultimate Tic-tac-toe")
grid = Grid(0,450,0,450,4)
smallGrid = [Grid(0,150,0,150,1)
			,Grid(0,150,150,300,1)
			,Grid(0,150,300,450,1)
			,Grid(150,300,0,150,1)
			,Grid(150,300,150,300,1)
			,Grid(150,300,300,450,1)
			,Grid(300,450,0,150,1)
			,Grid(300,450,150,300,1)
			,Grid(300,450,300,450,1)]
currentPos = (-1,-1)
currentSign = ['X','O']
currentColor = [(255,0,0),(0,0,255)]
curIndex = 0
board = np.full((9,3,3),None)
board_status = np.full(9,None)
surface.fill((0,0,0))
grid.draw(surface)
for g in smallGrid:
    g.draw(surface)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()

            bigPos = game.map_mouse_to_board(x,y,0,450,0,450)
            thisBigPos = bigPos[0] + 3*bigPos[1]
            #print(bigPos)
            correctInput = False
            if currentPos == (-1,-1):
                smallPos = game.map_mouse_to_board(x,y,bigPos[0]*150,bigPos[0]*150+150,bigPos[1]*150,bigPos[1]*150+150)
                correctInput = True
            elif currentPos == bigPos:
                smallPos = game.map_mouse_to_board(x,y,bigPos[0]*150,bigPos[0]*150+150,bigPos[1]*150,bigPos[1]*150+150)
                correctInput = True
                
            print(smallPos)
            if board[thisBigPos][smallPos[0]][smallPos[1]] == None and board_status[thisBigPos] == None and correctInput:
                currentPos = smallPos
                board[thisBigPos][smallPos[0]][smallPos[1]] = currentSign[curIndex]
                param = game.draw_square(smallPos,curIndex,bigPos,currentColor,surface)
                surface.blit(param[0],param[1])
                pygame.display.flip()
                if game.determine_win(thisBigPos,board)==True :
                    board_status[thisBigPos] = currentSign[curIndex]
                    if game.determine_big_win(board_status) == True:
                        for bigI in range(9):
                            for x in range(3):
                                for y in range(3):
                                    if board[bigI][x][y] == None:
                                        param = game.draw_square((x,y),curIndex,(bigI%3,bigI/3),currentColor,surface)
                                        surface.blit(param[0],param[1])
                                        pygame.display.flip()
                                        pygame.time.wait(1)

                if board_status[currentPos[0]+3*currentPos[1]] != None:
                    currentPos = (-1,-1)
                curIndex = curIndex * -1 + 1
            else:
                print(board[thisBigPos][smallPos[0]][smallPos[1]])
                print("Wrong input!")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                surface.fill((0,0,0))
                grid.draw(surface)
                for g in smallGrid:
                    g.draw(surface)
                pygame.display.flip()
                for i in range(9):
                    board_status[i] = None
                for i in range(9):
                    for x in range(3):
                        for y in range(3):
                            board[i][x][y] = None
                currentPos = (-1,-1)