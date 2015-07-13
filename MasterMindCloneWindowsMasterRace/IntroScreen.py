# -*- coding: utf-8 -*-
import pygame, sys, textrect
from pygame.locals import *
from pygame.sprite import *

pygame.init()

width = 1200
height = 700

display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()
FPS = 30
pygame.mixer.music.load("8bit sounds- Nes Legend of Zelda Main Theme (1).mp3")
pygame.mixer.music.play(-1, 0.0)

#colors
bg = (153,153,255)
buttonColor = (255, 255, 255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN =  (51,255,204)
#FONTS
#function to help us choose an installed font
def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names 
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
	
#create our font
font_preferences = [
        "CMU Sans Serif",
        "DejaVu Sans",
		"Arial"
		]
font = make_font(font_preferences, 24)

def update():
	pygame.display.update() 
	
class IntroScreen():

	soundBclicked = False

	def __init__(self, bx = width/2, by = height/2, bwidth=200, bheight= 100):
		self.borderColor = (51,102,255)
		self.borderRect = pygame.Rect(pygame.draw.rect(display, self.borderColor, ( bx-((bwidth+100)/2), by-(bheight*3/2)-50, bwidth+100, bheight*3+150  ), 3 ))
		self.font = font
		self.button_list = ['','','','']
		self.buttonColor = (255,255,255)
		self.bwidth = bwidth
		self.bheight = bheight
		self.bColorList = [self.buttonColor, self.buttonColor, self.buttonColor, GREEN]
		self.drawButtons()
		
	def drawButtons(self):
		self.button_list[0] =pygame.draw.rect(display, self.bColorList[0], (self.borderRect.left+50, self.borderRect.top+10, self.bwidth, self.bheight) )
		pygame.draw.rect(display, BLACK, (self.borderRect.left+50, self.borderRect.top+10, self.bwidth, self.bheight), 2 )
		self.button_list[1]=pygame.draw.rect(display, self.bColorList[1], (self.borderRect.left+50, self.borderRect.top+165, self.bwidth, self.bheight) )
		pygame.draw.rect(display, BLACK, (self.borderRect.left+50, self.borderRect.top+165, self.bwidth, self.bheight), 2 )
		self.button_list[2]=pygame.draw.rect(display, self.bColorList[2], (self.borderRect.left+50, self.borderRect.top+330, self.bwidth, self.bheight) )
		pygame.draw.rect(display, BLACK, (self.borderRect.left+50, self.borderRect.top+330, self.bwidth, self.bheight), 2 )
		self.textToButton("Έναρξη", self.button_list[0].left, self.button_list[0].top, self.button_list[0].width, self.button_list[0].height  )
		self.textToButton("Οδηγίες", self.button_list[1].left, self.button_list[1].top, self.button_list[1].width, self.button_list[1].height  )
		self.textToButton("About us", self.button_list[2].left, self.button_list[2].top, self.button_list[2].width, self.button_list[2].height  )
		#sound button k kala
		self.button_list[3]=pygame.draw.rect(display, self.bColorList[3], (width-160, 0, 160, 120))
		self.textToButton("Μουσική", width-160, 0, 160, 120) 
		
	def textToButton(self, text, bx, by, bwidth, bheight):
		textSurface = self.font.render(text, True, BLACK)
		textRect = textSurface.get_rect()
		textRect.center = (  bx + bwidth/2, by + bheight/2     )
		display.blit(textSurface, textRect)	
		
	def hoverButton(self):
			clicked = pygame.mouse.get_pressed()
			if self.button_list[0].collidepoint(pygame.mouse.get_pos()):
				self.bColorList[0]  = (102,255,51)
				self.drawButtons()
			elif self.button_list[1].collidepoint(pygame.mouse.get_pos()):
				self.bColorList[1]  = (102,255,51)
				self.drawButtons()
			elif self.button_list[2].collidepoint(pygame.mouse.get_pos()):
				self.bColorList[2]  = (102,255,51)
				self.drawButtons()
			elif self.button_list[3].collidepoint(pygame.mouse.get_pos()):
				if self.soundBclicked == False:
					self.bColorList[3]  =  GREEN
				else:
					self.bColorList[3]  = (245,0,61)
				self.drawButtons()
				update()
			else:
				self.bColorList = [self.buttonColor, self.buttonColor, self.buttonColor, self.bColorList[3]]
				self.drawButtons()
				update()
	
	
					
	def buttonClicked(self):
		clicked = pygame.mouse.get_pressed()
		if self.button_list[0].collidepoint(pygame.mouse.get_pos()):
			if clicked[0] == 1:
				return 0
		elif self.button_list[1].collidepoint(pygame.mouse.get_pos()):
			if clicked[0] == 1:
				return 1
		elif self.button_list[2].collidepoint(pygame.mouse.get_pos()):
			if clicked[0] == 1:
				return 2				
		elif self.button_list[3].collidepoint(pygame.mouse.get_pos()):
			if clicked[0] == 1:
				if self.soundBclicked == False:
					self.soundBclicked = True
				elif self.soundBclicked == True:
					self.soundBclicked = False
		return 3
		
	



	
def textToButton(text, bx, by, bwidth, bheight, color=BLACK):
		textSurface = font.render(text, True, color)
		textRect = textSurface.get_rect()
		textRect.center = (  bx + bwidth/2, by + bheight/2     )
		display.blit(textSurface, textRect)	
		

def logo():
	font_preferences = [
        "CMU Sans Serif",
        "DejaVu Sans",
		"Arial"
		]
	font = make_font(font_preferences, 52)
	#textToButton(,  0 ,0 , width, 200, )  #LOGO
	textSurface = font.render("Mastermind", True, (51,204,255))
	textRect = textSurface.get_rect()
	textRect.center = (   width/2,  80   )
	display.blit(textSurface, textRect)	

		
def instructions():
		display.fill(WHITE)
		bExitColor = (245,0,61)
		buttonExit = pygame.Rect( 0, height-100, 200, 100)
		instructionsLoop = True
		
		while instructionsLoop:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.quit()
					sys.exit()
				if ev.type == MOUSEMOTION:
					if buttonExit.collidepoint(pygame.mouse.get_pos()):
						bExitColor = (143,0,36)
					else:
						bExitColor = (245,0,61)
				if ev.type == MOUSEBUTTONDOWN:
					clicked = pygame.mouse.get_pressed()
					if buttonExit.collidepoint(pygame.mouse.get_pos()):
						if clicked[0] == 1:
							instructionsLoop = False
			stringText = 'Το Mastermind είναι παιχνίδι σπάσιμου κώδικα. Ο υπολογιστής θέτει τον κώδικα, ο οποίος αποτελείται από 4 "πούλια". Κάθε πούλι χαρακτηρίζεται από το χρώμα του και τη θέση του.  Ένα πούλι μπορεί να έχει 1 από 6 χρώματα, και σε κάθε κλειδί δύο ή περισσότερα πούλια μπορούν να έχουν το ίδιο χρώμα. Σκοπός του παιχνιδιού είναι ο παίχτης να μαντέψει το κλειδί που έχει θέσει ο υπολογιστής σε 8 ή λιγότερες προσπάθειες.'
			stringText+=	' Ο παίχτης αρχικά μαντέυει ένα κλειδί, τοποθετώντας στην πρώτη σειρά (ξεκινώντας από κάτω) του πίνακα τυχαία έναν συνδυασμό. Όταν ο συνδυασμός είναι έτοιμος, πατώντας το κουμπί  "Έλεγχος", ο παίχτης μπορεί να τσεκάρει πόσες σωστές επιλογές χρώματος και πόσες σωστές επιλογές χρώματος και σειράς έχει κάνει. Εάν ένας παίχτης έχει βρει το σωστό χρώμα και τη σωστή σειρά από ένα οποιοδήποτε πούλι, επιστρέφεται ένας μαύρος πόντος. Εάν ένας παίχτης έχει βάλει στην υπόθεσή του ένα πούλι, το χρώμα του οποίου υπάρχει μέσα στο κλείδι, αλλά το πούλι αυτό δεν βρίσκεται στην ίδια θέση με αυτή του κλειδιού, επιστρέφεται ένας άσπρος πόντος. Το παιχνίδι τελειώνει επιτυχώς, όταν επιστραφούν 4 μαύροι πόντοι, όποτε όλα τα πούλια βρίσκονται στην ίδια θέση και έχουν το ίδιο χρώμα με αυτό του κλειδιού.\nΠΡΟΣΟΧΗ: Οι άσπροι ή μαύροι πόντοι συμβολίζουν μόνο πόσες και όχι ποιες είναι οι σωστές υποθέσεις.'
			stringText+=	' Σε περίπτωση που μία υπόθεση είναι λάθος, μετά το πάτημα του "Έλεγχος", δίνεται μία νέα ευκαιρία στον παίχτη να βρει το σωστό κλειδί. Ο παίχτης πρέπει κάθε φορά να συγκρίνει κάθε υπόθεσή του με τις προηγούμενες και, μελετώντας τους άσπρους και μαύρους πόντους  που του επιστράφηκαν την εκάστοτε φορά, να καταλήξει στο σωστό αποτέλεσμα.'
			stringText +='\nΑν ο παίχτης θέλει να κλείσει τον ήχο, πρέπει να πατήσει πάνω στο κουμπί "Μουσική", το οποίο θα γίνει κόκκινο. Αντίστοιχα για να τον ενεργοποιήσει, αρκεί να το ξαναπατήσει και να γίνει πράσινο. '
			rectForText = pygame.draw.rect( display, (51,255,204) , (0, 0, width, height))
			text_color = (0,0,0)
			rendered_text = textrect.render_textrect(stringText, font, rectForText, text_color, (51,255,204),0)
			if rendered_text:
				display.blit(rendered_text, (rectForText.left, rectForText.top+50))
			pygame.draw.rect(display, bExitColor, buttonExit)
			textToButton("Πίσω", 0, height-100, 200, 100 )
			update()
	
def aboutUs():
		display.fill(WHITE)
		bExitColor = (245,0,61)
		buttonExit = pygame.Rect( 0, height-100, 200, 100)
		aboutUsLoop = True
		
		while aboutUsLoop:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.quit()
					sys.exit()
				if ev.type == MOUSEMOTION:
					if buttonExit.collidepoint(pygame.mouse.get_pos()):
						bExitColor = (143,0,36)
					else:
						bExitColor = (245,0,61)
				if ev.type == MOUSEBUTTONDOWN:
					clicked = pygame.mouse.get_pressed()
					if buttonExit.collidepoint(pygame.mouse.get_pos()):
						if clicked[0] == 1:
							aboutUsLoop = False
			stringText = "About US"
			rectForText = pygame.draw.rect( display, (51,255,204) , (0, 0, width, height))
			text_color = (0,0,0)
			rendered_text = textrect.render_textrect(stringText, font, rectForText, text_color, (51,255,204),1)
			if rendered_text:
				display.blit(rendered_text, (rectForText.left, rectForText.centery-200))
			pygame.draw.rect(display, bExitColor, buttonExit)
			textToButton("Πίσω", 0, height-100, 200, 100 )
			update()

	

#logic == none. Exeis enan counter o opoios isoutai me 3, kai etsi trexei h loopa. otan patas ena apo ta koubia
# allazei o arithmos tou, analoga me to pio koubi patises. an patiseis p.x instructions ginete 1 gia na bei mesa 
# sto menu odigies, kai meta gamiete h panagia. otan patiseis pisw, ksanaginete 3 gia na sinexisei na trexei to intro.

#oi idigies kai to about us einai 2 ksexoristes loopes, oste na einai san ksexoristh othoni. meta apo kathe eksodo apo autes, prepei na ginei ena .fill gia na exoume aspro xroma, kai na ksanadimiourgithoun ta koubia, oste na einai omorfa
#kai sto swsto plaisio.
def main():
	
	counter = 3 #counter == 3 trexei h main. counter == 0 main paixnidi. counter == 1 odigies. counter ==2, about us.
	display.fill(buttonColor)		
	intro = IntroScreen()
	logo()
	gameRunning = True
	while gameRunning:
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEMOTION:
				intro.hoverButton() #an to mouse einai panw apo ta koubia allakseta xrwma
			if event.type == MOUSEBUTTONDOWN:
				counter = intro.buttonClicked() #an to mouse clickarei kapio apo ta koubia prakse analoga.
			
		if counter == 0:
			gameRunning = False
		elif counter == 1:
			instructions() #afotou vgeis apo to instructions, ksana gemizeis tn othoni xroma, kai ksanadimiougeis ta koubia oste na einai omorfa ola kai wraia nikokoiremena.
			display.fill(buttonColor)
			intro = IntroScreen()
			update()
			counter = 3
		elif counter == 2:
			aboutUs()
			display.fill(buttonColor)
			intro = IntroScreen()
			update()
			counter = 3
		if counter == 3:
			gameRunning = True
		
		if intro.soundBclicked == True:
			pygame.mixer.music.pause()
		elif intro.soundBclicked == False:
			pygame.mixer.music.unpause()
		clock.tick(240)
		
		update()
	

	
