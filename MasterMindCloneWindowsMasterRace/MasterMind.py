 # -*- coding: utf-8 -*-
import pygame, sys, textrect
import modules
import IntroScreen
import random
from pygame.locals import *

pygame.init()

width = 1200
height = 700

display = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
FPS = 60




def update():
	pygame.display.update() 
	
	
pygame.display.set_caption("Mastermind")

#colors
bg = (153,153,255)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
YELLOW = (247, 233, 69)
GREEN =  (51,255,204)

IntroScreen.main()
display.fill(bg)

soundRect = [''] #soundrect as a list
blackDot = modules.BlackPeg(100, 200)
whiteDot = modules.WhitePeg(100, 250)
x = 300


block_list = pygame.sprite.OrderedUpdates() #think of it as an ordered list of sprites.  gg wp qq
#pegs  
yellowPeg = modules.YellowPeg(width-350, x)
block_list.add(yellowPeg)
redPeg = modules.RedPeg(width-350, x+40)
block_list.add(redPeg)
bluePeg = modules.BluePeg(width-350, x+80)
block_list.add(bluePeg)
purplePeg = modules.PurplePeg(width-350, x+120)
block_list.add(purplePeg)
greenPeg = modules.GreenPeg(width-350, x+160)
block_list.add(greenPeg)
orangePeg = modules.OrangePeg(width-350, x+200)
block_list.add(orangePeg)

resultList = ['','','','']
#ai lel ex di
def ai():
	listofColors = ["yellow", "red", "blue", "purple", "green", "orange"]
	for i in range(4):
		resultList[i] =  listofColors[random.randint(0,5)]
	temporarySetresult = set(resultList)
	#print(resultList)
	while len(temporarySetresult) <=2:
		for i in range(len(listofColors)):
			while resultList.count(listofColors[i]) >= 3:
				for i in range(4):
					resultList[i] =  listofColors[random.randint(0,5)]
		
			
		
		
	
	
#lel ai ex di answer check peg update, no idea kappa
def updateAswerBox(black, white, y):
	x = 105
	for i in range(black):
		display.blit(blackDot.getImage(),(x,y-5) )
		x+=40
	for i in range(white):
		display.blit(whiteDot.getImage(),(x,y-5) )	
		x+=40
	
	
	
#function to help us choose an installed font
def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names 
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
	


	
def losingMessage(text):	
	font_preferences = [
        "CMU Sans Serif",
        "DejaVu Sans",
		"Arial"
		]
	font = make_font(font_preferences, 54)	
	textSurface = font.render(text, True, BLACK)
	textRect = textSurface.get_rect()
	textRect.center = ( width/2-50,  50  )
	display.blit(textSurface, textRect)
	update()
	pygame.time.delay(4000)
	display.fill(bg, textRect )
	update()
	
	
	
def warningMessage(text):
	#create our font
	font_preferences = [
        "CMU Sans Serif",
        "DejaVu Sans",
		"Arial"
		]
	font = make_font(font_preferences, 32)	
	textSurface = font.render(text, True, BLACK)
	textRect = textSurface.get_rect()
	textRect.center = (   width/2-50,  50    )
	display.blit(textSurface, textRect)
	update()
	pygame.time.delay(1000)
	display.fill(bg, textRect )
	update()

def winMessage():
	text = "Νενικήκαμεννννννννννννννννν!!"
	#create our font
	font_preferences = [
        "CMU Sans Serif",
        "DejaVu Sans",
		"Arial"
		]
	font = make_font(font_preferences, 54)	
	textSurface = font.render(text, True, BLACK)
	textRect = textSurface.get_rect()
	textRect.center = (   width/2-50,  height/2    )
	display.blit(textSurface, textRect)
	update()
	pygame.time.delay(1500)
	update()

	
def drawPegs():
	for i in range(6):
		block_list.sprites()[i].draw(display)
	

	
def createRectRow():
	
	y = height-140
	for i in range(8):
		x = width/2-200
		pygame.draw.rect(display, YELLOW, (100, y, 200, 60))
		pygame.draw.rect(display, GREEN, (100, y, 200, 60), 2)
		for j in range(4):
			rectRowList.append(pygame.Rect(x , y , 100 ,60))
			pygame.draw.rect(display, WHITE, rectRowList[j+4*i])
			pygame.draw.rect(display, GREEN, rectRowList[j+4*i], 2)
			x+=100
			update()
		y -= 60	
		
#isos metaferthei kai ginei class p tha klironomei apo tn super class. isos kai oxi. kaneis dn kserei.			
def soundButton(color):
	font_preferences = [
        "CMU Sans Serif",
        "DejaVu Sans",
		"Arial"
		]
	font = make_font(font_preferences, 24)
	soundRect[0] =  pygame.draw.rect(display, color, (width-160, 0, 160, 120))
	textSurface = font.render("Μουσική", True, BLACK)
	textRect = textSurface.get_rect()
	textRect.center = (  width-160 + 160/2, 120/2     )
	display.blit(textSurface, textRect)		
	
	
	
		
imagesList = []		
def getImages():
	for i in range(6):
		imagesList.append(block_list.sprites()[i].getImage())
rectRowList = []
counter = 0
pegSelected  = []


drawPegs()
getImages()

answerList = ['','','','']
counterTries = 0
numberOfTries = 8
createRectRow()
ai()
answersY = 580
bakalika = 0

#sound control
soundBclicked = False
butt = modules.restartButton(display, GREEN, width-200, height/2-50, 140, 80, )
buttonExit = modules.exitButton(display, (245,0,61), width-200, height/2+50, 140, 80, )
while True:
	
	numberOfWhitePegs = 0
	numberOfBlackPegs = 0
	if numberOfTries == 0:
		losingMessage("Δυστυχώς έχασες.")
	
		pygame.quit()
		sys.exit()
	if counterTries == 1:
		del rectRowList[0:4]
		counterTries = 0
	for ev in pygame.event.get():
		if ev.type == QUIT:
			pygame.quit()
			sys.exit()
		if ev.type == MOUSEBUTTONDOWN:
			if buttonExit.isClicked():
				pygame.quit()
				sys.exit()
			if soundRect[0].collidepoint(pygame.mouse.get_pos()):
				if soundBclicked == False:
					soundBclicked = True
				elif soundBclicked == True:
					soundBclicked = False
			
			isClicked = butt.isClicked()
			if isClicked == True:
				if '' in answerList :
					warningMessage("Πρέπει να συμπληρώσεις και τα 4 τετράγωνα για να προχωρήσεις!!")
					break
				numberOfTries  -= 1
				setResult = list(set(resultList))
				print(setResult)
				if (len(setResult)) == 3:      #an exoume stn lush to idio xrwma panw apo mia fora
					for i in range(len(resultList)):
						if resultList[i] in answerList:
							numberOfWhitePegs+=1
					for i in range(len(resultList)):
						if resultList[i] == answerList[i]:
							numberOfBlackPegs += 1
							numberOfWhitePegs -= 1
					if numberOfBlackPegs == 2 and numberOfWhitePegs >=2:
						numberOfWhitePegs = 2
					elif numberOfBlackPegs == 3 and numberOfWhitePegs >=2:
						numberOfWhitePegs = 1
					elif  numberOfBlackPegs == 4:
						numberOfWhitePegs = 0
					updateAswerBox(numberOfBlackPegs, numberOfWhitePegs, answersY)
					answersY -= 60
					counterTries = 1
					answerList = ['','','','']
				else:
					for i in range(len(setResult)):
						if setResult[i] in answerList:
							numberOfWhitePegs+=1
					for i in range(len(resultList)):
						if resultList[i] == answerList[i]:
							numberOfBlackPegs += 1
							numberOfWhitePegs -= 1
					updateAswerBox(numberOfBlackPegs, numberOfWhitePegs, answersY)
					answersY -= 60
					counterTries = 1
					answerList = ['','','','']
					
					
				
				
			for i in range(6):
				if block_list.sprites()[i].checkMouse():
					pegSelected = block_list.sprites()[i].checkMouse()
			# ------------------------
			for i in range(4):
				if rectRowList[i].collidepoint(pygame.mouse.get_pos()):
					clicked = pygame.mouse.get_pressed()
					if clicked[0] == 1 and pegSelected:
						if pegSelected == "yellow":
							display.blit(imagesList[0], (rectRowList[i].centerx-26 , rectRowList[i].centery-26   ))
							answerList[i] = (pegSelected)
						elif pegSelected == "red":
							display.blit(imagesList[1], (rectRowList[i].centerx-26 , rectRowList[i].centery-26    ))
							answerList[i] = (pegSelected)
						elif pegSelected == "blue":
							display.blit(imagesList[2], (rectRowList[i].centerx-26 , rectRowList[i].centery-26    ))
							answerList[i] = (pegSelected)
						elif pegSelected == "purple":
							display.blit(imagesList[3], (rectRowList[i].centerx-26 , rectRowList[i].centery-26    ))
							answerList[i] = (pegSelected)
						elif pegSelected == "green":
							display.blit(imagesList[4], (rectRowList[i].centerx-26 , rectRowList[i].centery-26    ))
							answerList[i] = (pegSelected)
						elif pegSelected == "orange":
							display.blit(imagesList[5], (rectRowList[i].centerx-26 , rectRowList[i].centery-26    ))
							answerList[i] = (pegSelected)
							
						pegSelected  = []
		
		if ev.type == MOUSEMOTION:
			butt.hover()
			buttonExit.hover()
		#debugging
		if ev.type == KEYDOWN:
			if ev.key == K_q:
				pass
			if ev.key == K_s:
				print(resultList)
			if ev.key == K_d:
				if '' in answerList :
					warningMessage('l')
					break
				setResult = list(set(resultList))
				for i in range(len(setResult)):
					if bakalika == 1:
						pass
					if setResult[i] in answerList:
						numberOfWhitePegs+=1
				for i in range(len(resultList)):
					if resultList[i] == answerList[i]:
						numberOfBlackPegs += 1
						#numberOfWhitePegs -= 1
				#print(answerList)
				#print(resultList)
				updateAswerBox(numberOfBlackPegs, numberOfWhitePegs, answersY)
				answersY -= 60
				counterTries = 1
				
				answerList = ['','','','']
			



	
	
	clock.tick(FPS)
	if soundBclicked == False:
		soundButton(GREEN)
		pygame.mixer.music.unpause()
	elif soundBclicked == True:
		soundButton((245,0,61))
		pygame.mixer.music.pause()
	
	butt.drawButton()
	buttonExit.drawButton()
	butt.textToButton("Έλεγχος")
	buttonExit.textToButton("Έξοδος")
	update()
	if numberOfBlackPegs == 4:
		winMessage()
		pygame.quit()
		sys.exit()

