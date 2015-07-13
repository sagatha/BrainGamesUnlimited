from button import *
import sys, pygame
from pygame.locals import *
from random import randint
import math

#displays several diffirent patterns in 1 sec intervals to confuse the player (recreates the button grid and randomizes the patterns)
def showShuffle(my_screen,HORIZ,VERT,level,pattern_num):
	
	dt = pygame.time.get_ticks()
	time_elapsed=0
	while  time_elapsed<1500:
	     
		dt2=pygame.time.get_ticks()
		time_elapsed+=dt2-dt
		dt=dt2
		#shuffle
		width=50
		height=50
		x_offset=HORIZ/int(math.sqrt(level))
		y_offset=VERT/int(math.sqrt(level))
		patternlistTemp=[]
		for i in range (0,level):
			patternlistTemp.append(0)
		i=1
		while i<=pattern_num:
			randomNum=randint(0,level-1)
			if patternlistTemp[randomNum]==0:
				patternlistTemp[randomNum]=1
				i+=1
		
		imageBlue=pygame.image.load('images/blue.png')
		imageBlue=pygame.transform.scale(imageBlue,(50,50))
		imageRed=pygame.image.load('images/red.png')
		imageRed=pygame.transform.scale(imageRed,(50,50))
		id_counter=0
		for i in range (0,int(math.sqrt(level))):
			for j in range (0,int(math.sqrt(level))):
				my_rect=pygame.Rect(x_offset,y_offset,width, height)
				if(patternlistTemp[id_counter]==1):			
					my_screen.blit(imageRed,my_rect)		
				else:
					my_screen.blit(imageBlue,my_rect)
				id_counter+=1
				x_offset+=width+20
			y_offset+=height+20
			x_offset=HORIZ/int(math.sqrt(level))
		pygame.time.delay(100)
		pygame.display.update()

#function that initiates the random pattern and displays it to the player . Returns a vector with the correct pattern
def initiatePattern(my_screen,HORIZ,VERT,level,pattern_num):
	
	width=50
	height=50
	x_offset=HORIZ/int(math.sqrt(level))
	y_offset=VERT/int(math.sqrt(level))

	#create random pattern vector
	patternlist=[]
	for i in range (0,level):
		patternlist.append(0)
	i=1
	while i<=pattern_num:
		randomNum=randint(0,level-1)
		if patternlist[randomNum]==0:
			patternlist[randomNum]=1
			i+=1

	#load button pictures
	imageBlue=pygame.image.load('images/blue.png')
	imageBlue=pygame.transform.scale(imageBlue,(50,50))
	imageRed=pygame.image.load('images/red.png')
	imageRed=pygame.transform.scale(imageRed,(50,50))
	id_counter=0
	#display pattern
	for i in range (0,int(math.sqrt(level))):
		for j in range (0,int(math.sqrt(level))):
			my_rect=pygame.Rect(x_offset,y_offset,width, height)
			if(patternlist[id_counter]==1):			
				my_screen.blit(imageRed,my_rect)		
			else:
				my_screen.blit(imageBlue,my_rect)
			id_counter+=1
			x_offset+=width+20
		y_offset+=height+20
		x_offset=HORIZ/int(math.sqrt(level))
	
	pygame.display.update()
	pygame.time.delay(pattern_num*500)
	showShuffle(my_screen,HORIZ,VERT,level,pattern_num)
	return patternlist
