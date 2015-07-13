import pygame,sys
from pygame.locals import *
 
pygame.init()
 
 
class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=80,font_color=(255,255,255), (pos_x, pos_y)=(0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
    
    
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, color):
        self.font_color = color
        self.label = self.render(self.text, 1, self.font_color)
 
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
 
 
class GameMenu():
    def __init__(self, screen, items, font=None, font_size=30,
                    font_color=color):
        self.screen = screen
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
	self.font_color = font_color
 	self.labels=[]
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item)
 
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.width / 2) - (menu_item.width / 2)
            pos_y = (self.height / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)
 
            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
 	    self.labels.append(item)
    
    def run(self):
        
        while True:
            for ev in pygame.event.get():
		if ev.type==QUIT:
			pygame.quit()
			sys.exit()
		if ev.type==MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					for index, item in enumerate(self.items):
                				if item.is_mouse_selection(pygame.mouse.get_pos()):
							if self.labels[index]=='Start':
								return True
                					else:
								return False
						
 
            for item in self.items:
                if item.is_mouse_selection(pygame.mouse.get_pos()):
                    item.set_font_color((255, 0, 0))
                else:
                    item.set_font_color((255, 255, 255))
                    
                self.screen.blit(item.label, item.position)
 
            pygame.display.update()
 
 

