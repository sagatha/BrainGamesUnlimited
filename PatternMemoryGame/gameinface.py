from button import *
import sys, pygame
from pygame.locals import *
import playscreen
import patternInitiation
from GameMenu import *

#game's master function. handles the pattern initiation screen , the user input interface, and the game and level menu

pygame.init()
HORIZ=600
VERT=600

#create menu screen
menu_items = ('Start', 'Quit')
image=pygame.image.load('images/background.png')
image=pygame.transform.scale(image,(HORIZ,VERT))
my_screen=pygame.display.set_mode((HORIZ,VERT), 0,32)
my_screen.blit(image, [0, 0])
pygame.display.set_caption('Game Menu')
my_font=pygame.font.SysFont(None,64)
        
def printlife(surf,life):
	position=550
	image=pygame.image.load('images/heart.png')
	image=pygame.transform.scale(image,(50,50))
        for l in range(0,life):  
        	surf.blit(image, (position-l*40, 20))
		

#functions that change the difficulty based on current level
def getBlockNumber(gameLevel):
	if gameLevel<3:
		level=9
	elif gameLevel<7:
		level=16
	elif gameLevel<10:
		level=25
	return level

def getPatternSize(gameLevel):
	if gameLevel<3:
		pattern_num=3
	elif gameLevel<5:
		pattern_num=4
	elif gameLevel<7:
		pattern_num=5
	elif gameLevel<8:
		pattern_num=6
	elif gameLevel<10:
		pattern_num=7
	return pattern_num

def centerFont(my_screen,my_text):
	centX = my_screen.get_rect().centerx
	centY = my_screen.get_rect().centery
	
	my_textRect = my_text.get_rect()         
   	my_textRect.centerx = centX          
        my_textRect.centery = centY
	return my_textRect

#start game function
def play():
	game = GameMenu(my_screen, menu_items)
	start=game.run()
	while start:
	#create screen
		my_screen.blit(image, [0, 0])	
		pygame.display.set_caption('Remember the Pattern')
		gameLevel=1
		life=3
		while gameLevel<10:

			#show current level
			level_str='Level '+ str(gameLevel)
			my_text=my_font.render(level_str,True,(255,255,255))
			my_screen.blit(image, [0, 0])
			my_screen.blit(my_text, centerFont(my_screen,my_text))
			pygame.display.update()
			pygame.time.delay(2000)
			my_screen.blit(image, [0, 0])
			printlife(my_screen,life)
			
			#create and display pattern
			pattern_size=getPatternSize(gameLevel)
			block_number=getBlockNumber(gameLevel)
			patternlist = patternInitiation.initiatePattern(my_screen,HORIZ,VERT,block_number,pattern_size)
			my_screen.blit(image, [0, 0])
			printlife(my_screen,life)
		
			#ask user and show user input interface
			buttonlist=playscreen.initiateGameScreen(my_screen,HORIZ,VERT,block_number,pattern_size)
			
			#compare the input with the initial pattern and show a message based on the result
			flag=True
			for i in range(0,block_number-1):
				if not patternlist[i]==buttonlist[i].getIsPressed():
					flag=False
					break
			if flag:	
				my_text=my_font.render('CORRECT!',True,(255,255,255))
				gameLevel+=1
			else:
				my_text=my_font.render('Level Failed',True,(255,255,255))
				life-=1
			if life==0:
				my_text=my_font.render('Game Over!',True,(255,255,255))
				my_screen.blit(image, [0, 0])
				my_screen.blit(my_text, centerFont(my_screen,my_text))
				pygame.display.update()
				pygame.time.delay(2000)
				break
	
			#show message on screen
			my_screen.blit(image, [0, 0])
			my_screen.blit(my_text, centerFont(my_screen,my_text))
			pygame.display.update()
			pygame.time.delay(2000)
		
		#show menu after finishing the game
		my_screen.blit(image, [0, 0])
		pygame.display.set_caption('Game Menu')
		game = GameMenu(my_screen, menu_items)
		start=game.run()
		
	else:
		#say bye
		my_text=my_font.render('BYE!!',True,(255,255,255))
		my_screen.blit(image, [0, 0])
		my_screen.blit(my_text, centerFont(my_screen,my_text))
		pygame.display.update()
		pygame.time.delay(4000)
	
	
play()
