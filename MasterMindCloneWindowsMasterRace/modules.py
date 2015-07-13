 # -*- coding: utf-8 -*-
import pygame, sys, textrect
from pygame.locals import *
from pygame.sprite import *

pygame.init()

width = 1200
height = 700

display = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
FPS = 60


def update():
    pygame.display.update() 
    
    
pygame.display.set_caption("Test Game")

#colors
bg = (153,153,255)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

#super class of all pegs
class Pegs(Sprite):
    
    def __init__(self, createX, createY, dimX=36, dimY=36):
        Sprite.__init__(self)
        self.rect = pygame.Rect(createX, createY, dimX, dimY)
        self.image = pygame.image.load("black_dot.png")

    def draw(self, surface):
        pass

class BlackPeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("black_dot.png")
            
        def draw(self, surface):
            display.blit(self.image, self)
            
        def getImage(self):
            return self.image   
            
class WhitePeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("white_dot.png")
            
        def draw(self, surface):
            display.blit(self.image, self)
            
        def getImage(self):
            return self.image   
            
class YellowPeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("yellowPeg.png")
            
        def draw(self, surface):
            display.blit(self.image, self)
            
        def checkMouse(self):
            clicked = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked[0] == 1:
                    return "yellow"
                    
        def getImage(self):
            return self.image
            
        def getColor(self):
            return "yellow"
            
class RedPeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("redPeg.png")
            
        def draw(self, surface):
            display.blit(self.image, self)

        def checkMouse(self):
            clicked = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked[0] == 1:
                    return "red"
                    
        def getImage(self):
            return self.image   
            
        def getColor(self):
            return "red"
            

class BluePeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("bluePeg.png")
            
        def draw(self, surface):
            display.blit(self.image, self)
            
        
        def checkMouse(self):
            clicked = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked[0] == 1:
                    return "blue"       
            
        def getImage(self):
            return self.image   
            
        def getColor(self):
            return "blue"

class OrangePeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("orangePeg.png")
            
        def draw(self, surface):
            display.blit(self.image, self)
            
        def checkMouse(self):
            clicked = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked[0] == 1:
                    return "orange"     
        
            
        def getImage(self):
            return self.image               
            
        def getColor(self):
            return "orange"

class GreenPeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("greenPeg.png")
            
        def draw(self, surface):
            display.blit(self.image, self)
            
            
        def checkMouse(self):
            clicked = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked[0] == 1:
                    return "green"          
            
            
        def getImage(self):
            return self.image   

        def getColor(self):
            return "green"

class PurplePeg(Pegs):
        def __init__(self, createX, createY, dimX=36, dimY=36):
            Pegs.__init__(self, createX, createY, dimX, dimY)
            self.image = pygame.image.load("purplePeg.png")
            
        def draw(self, surface):
            display.blit(self.image, self)  
            
        def getImage(self):
            return self.image               
            
            
        def checkMouse(self):
            clicked = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked[0] == 1:
                    return "purple"         
    
        def getColor(self):
            return "purple"
            
            
# button super class and derived classes
class Button(pygame.Rect):
		
		#create our font
		font_preferences = [
				"CMU Sans Serif",
				"DejaVu Sans",
				"Arial"
				]
		
		def __init__(self, surf, color, createX, createY, dimX, dimY):
			pygame.Rect.__init__(self, createX, createY, dimX, dimY) 
			self.font = self.make_font(self.font_preferences, 24)
			self.bx = createX
			self.by = createY
			self.bwidth = dimX
			self.bheight = dimY
			self.color = color
			self.surface = surf
			
		def make_font(self, fonts, size):
			available = pygame.font.get_fonts()
			# get_fonts() returns a list of lowercase spaceless font names 
			choices = map(lambda x:x.lower().replace(' ', ''), fonts)
			for choice in choices:
				if choice in available:
					return pygame.font.SysFont(choice, size)
			return pygame.font.Font(None, size)
		
		def textToButton(self, text):
			textSurface = self.font.render(text, True, BLACK)
			textRect = textSurface.get_rect()
			textRect.center = (  self.bx + self.bwidth/2, self.by + self.bheight/2)
			display.blit(textSurface, textRect)
			
		def drawButton(self):
			pygame.draw.rect(self.surface, self.color, self, 0)
			
		def hover(self):
			if self.collidepoint(pygame.mouse.get_pos()):
				self.color = (100,200,50)
			else:
				self.color = (51,255,204)
				
		def isClicked(self):
			clicked = pygame.mouse.get_pressed()
			if self.collidepoint(pygame.mouse.get_pos()):
				if clicked[0] == 1:
					return True
				else: return False
			return False
class exitButton(Button):
		def __init__(self, *args):
			Button.__init__(self, *args)
			
		def hover(self):
			if self.collidepoint(pygame.mouse.get_pos()):
				self.color = (100,200,50)
			else:
				self.color = (245,0,61)
			
			
class restartButton(Button):
		def __init__(self, *args):
			Button.__init__(self, *args)			
			
		
		

			 
			 


            

   
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        