import sys, pygame
from pygame.locals import *
from pygame.transform import scale
# class that is used as a button on the pattern grid , contains variables regarding if the button is pressed, its current state , size and position
class Button():

	def __init__(self,myid,surf,x,y,width,height):
		color=(255,255,255)		
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.myrect=pygame.Rect(x,y,width,height)
		self.imageRed=pygame.image.load('images/red.png')
		self.imageRed=pygame.transform.scale(self.imageRed,(50,50))
		self.imageBlueLight=pygame.image.load('images/bluelight.png')
		self.imageBlueLight=pygame.transform.scale(self.imageBlueLight,(50,50))
		self.imageBlue=pygame.image.load('images/blue.png')
		self.imageBlue=pygame.transform.scale(self.imageBlue,(50,50))
		
		self.buttonid=myid
		self.ispressed=False
		self.surf=surf
		surf.blit(self.imageBlue,self.myrect)
	
	#checks if the button got pressed and if yes it changes its color and variable @ispressed
	def gotPressed(self,position):
		if self.myrect.collidepoint(position) and not self.ispressed:
			self.surf.blit(self.imageRed,self.myrect)			
			self.ispressed=True			
			return True
		else:
			return False

	#checks if the mouse is over the button and if yes it changes its color (highlight)	
	def collides(self, position):

		if self.myrect.collidepoint(position) and self.ispressed==False:		
			self.surf.blit(self.imageBlueLight,self.myrect)			
		elif self.ispressed==False:
			self.surf.blit(self.imageBlue,self.myrect)			
	
	#returns 1 or 0 depending on the button's ispressed state.
	def getIsPressed(self):
		if self.ispressed:
			return 1
		else:
			return 0
