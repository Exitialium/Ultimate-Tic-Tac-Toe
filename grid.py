import pygame

class Grid:
	
	def __init__(self,iright,ileft,itop,ibuttom,ithickness):
		right = iright
		left = ileft
		top = itop
		buttom = ibuttom
		self.thickness = ithickness
		self.grid_lines = [((right,(buttom-top)/3+top),(left,(buttom-top)/3+top)),
						((right,((buttom-top)*2)/3+top),(left,((buttom-top)*2)/3+top)),
						((((left-right)*2)/3+right,top),(((left-right)*2)/3+right,buttom)),
						((((left-right))/3+right,top),(((left-right))/3+right,buttom ))]
		self.margin = [((1,1),(left,1)),((0,0),(0,buttom)),((left,0),(left,buttom)),((0,buttom),(left,buttom))]
	def draw(self, surface):
		for line in self.grid_lines:
			pygame.draw.line(surface, (200,200,200), line[0], line[1], self.thickness)
		if self.thickness>1:
			for line in self.margin:
				pygame.draw.line(surface, (200,200,200), line[0], line[1], int(self.thickness))