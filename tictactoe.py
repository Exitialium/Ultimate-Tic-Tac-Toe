import pygame
import numpy as np

class GameModel:
    def getHash(self,board):
        boardHash = str(board.reshape(9 * 3 * 3))
        return boardHash
	def map_mouse_to_board(self,x,y,l,r,t,b):
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

	def determine_win(self,bigInd,board):
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
	def determine_big_win(self,board_status):
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

	def draw_square(self,smallPos,curIndex,bigPos,currentColor,surface):
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
		return (surf,(surfX,surfY))

	def init(self,surface,grid,smallGrid):
		surface.fill((0,0,0))
		grid.draw(surface)
		for g in smallGrid:
			g.draw(surface)
		return surface




	
	

	

	
	
	





				


			




	