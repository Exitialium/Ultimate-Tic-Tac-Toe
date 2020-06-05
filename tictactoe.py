import pygame
from grid import Grid

def map_mouse_to_board(x,y,l,r,t,b):
	bigPosX = -1
	bigPosY = -1
	#print("x:"+str(x)+" y:"+str(y))
	if x >= l and x < (r-l)/3 + l:
		bigPosX = 0
	elif x >= (r-l)/3 + l and x < (2*(r-l))/3 + l:
		bigPosX = 1
	elif x >= (2*(r-l))/3 + l and x < r:
		bigPosX = 2

	if y >= t and y < (b-t)/3 + t:
		bigPosY = 0
	elif y >= (b-t)/3 + t and y < 2*(b-t)/3 + t:
		bigPosY = 1
	elif y >= 2*(b-t)/3 + t and y < b:
		bigPosY = 2

	return (bigPosX,bigPosY)


def determine_win(bigInd):
	#horizontal
	for y in range(3):
		if board[bigInd][y][0] == board[bigInd][y][1] and board[bigInd][y][2] == board[bigInd][y][1] and board[bigInd][y][0]!= None:
			return True
	#vertical
	for y in range(3):
		if board[bigInd][0][y] == board[bigInd][1][y] and board[bigInd][1][y] == board[bigInd][2][y] and board[bigInd][0][y]!= None:
			return True
	#diagonal
	if board[bigInd][0][0] == board[bigInd][1][1] and board[bigInd][2][2] == board[bigInd][1][1] and board[bigInd][1][1] != None:
		return True
	if board[bigInd][2][0] == board[bigInd][1][1] and board[bigInd][2][0] == board[bigInd][0][2] and board[bigInd][1][1] != None:
		return True

	return False

def determine_big_win():
	#horizontal
	for y in range(3):
		if board_status[3*y] == board_status[3*y+1] and board_status[3*y+1] == board_status[3*y+2] and board_status[3*y] != None:
			return True
	#vertical
	for y in range(3):
		if board_status[y] == board_status[y+3] and board_status[y+3] == board_status[y+6] and board_status[y] != None:
			return True
	#diagonal
	if board_status[0] == board_status[4] and board_status[4] == board_status[8] and board_status[0] != None:
		return True
	if board_status[2] == board_status[4] and board_status[4] == board_status[6] and board_status[6] != None:
		return True

	return False

def draw_square(smallPos,curIndex,bigPos):
	width = 49
	length = 49
	if smallPos[0]==2:
		width = 48
	if smallPos[1]==2:
		length = 48
	if smallPos[0]==0:
		width = 47
	if smallPos[1]==0:
		length = 47
	surf = pygame.Surface((width,length))
	surf.fill(currentColor[curIndex])
	surfX = bigPos[0]*150+smallPos[0]*50+1
	surfY = bigPos[1]*150+smallPos[1]*50+1
	if smallPos[0] == 0:
		surfX += 2
	if smallPos[1] == 0:
		surfY += 2
	surface.blit(surf,(surfX,surfY))
	pygame.display.flip()

def init():
	surface.fill((0,0,0))
	grid.draw(surface)
	for g in smallGrid:
		g.draw(surface)
	pygame.display.flip()




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
running = True;

currentPos = (-1,-1)
currentSign = ['X','O']
currentColor = [(255,0,0),(0,0,255)]
curIndex = 0

board = [
		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]],

		[[None,None,None],
		[None,None,None],
		[None,None,None]]
		]


board_status = [None,None,None,None,None,None,None,None,None]
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

			bigPos = map_mouse_to_board(x,y,0,450,0,450)
			thisBigPos = bigPos[0] + 3*bigPos[1]
			#print(bigPos)
			correctInput = False
			if currentPos == (-1,-1):
				smallPos = map_mouse_to_board(x,y,bigPos[0]*150,bigPos[0]*150+150,bigPos[1]*150,bigPos[1]*150+150)
				correctInput = True
			elif currentPos == bigPos:
				smallPos = map_mouse_to_board(x,y,bigPos[0]*150,bigPos[0]*150+150,bigPos[1]*150,bigPos[1]*150+150)
				correctInput = True
				
			print(smallPos)
			if board[thisBigPos][smallPos[0]][smallPos[1]] == None and board_status[thisBigPos] == None and correctInput:
				currentPos = smallPos
				board[thisBigPos][smallPos[0]][smallPos[1]] = currentSign[curIndex]
				draw_square(smallPos,curIndex,bigPos)
				if determine_win(thisBigPos)==True :
					board_status[thisBigPos] = currentSign[curIndex]
					if determine_big_win() == True:
						for bigI in range(9):
							for x in range(3):
								for y in range(3):
									if board[bigI][x][y] == None:
										draw_square((x,y),curIndex,(bigI%3,bigI/3))
										pygame.time.wait(1)

				if board_status[currentPos[0]+3*currentPos[1]] != None:
					currentPos = (-1,-1)
				curIndex = curIndex * -1 + 1
			else:
				print(board[thisBigPos][smallPos[0]][smallPos[1]])
				print("Wrong input!")
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				init()
				for i in range(9):
					board_status[i] = None
				for i in range(9):
					for x in range(3):
						for y in range(3):
							board[i][x][y] = None
				currentPos = (-1,-1)





				


			




	