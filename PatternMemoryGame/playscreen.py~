from button import *
import sys, pygame
from pygame.locals import *
import math
def display_time(my_screen,time_elapsed,max_time):
	x=560
	y=80
	width=30
	height=30
	elapsed_counter=0
	for i in range (0,max_time/1000):
		imagetemp1=pygame.image.load('images/clock_red.png')
		image_clock_red=pygame.transform.scale(imagetemp1,(width,height))
		imagetemp2=pygame.image.load('images/clock_black.png')
		image_clock_black=pygame.transform.scale(imagetemp2,(width,height))

		if elapsed_counter<time_elapsed/1000:
			myrect=pygame.Rect(x,y,width,height)
			my_screen.blit(image_clock_red,myrect)
			elapsed_counter+=1
		else:
			myrect=pygame.Rect(x,y,width,height)
			my_screen.blit(image_clock_black,myrect)
		x-=width+5



def checkpressed(myButtons,position):
	for b in myButtons:
		if b.gotPressed(position):
			return True

def checkmouseovers(myButtons,position):
	for b in myButtons:
		b.collides(position)

#initializes the player input interface. Returns a vector of all the buttons and their current condition (pressed or not)
def initiateGameScreen(my_screen,HORIZ,VERT,level,pattern_num):
	#create buttons and add them to a list
	id_count=0
	myButtons=[]
	x_offset=HORIZ/int(math.sqrt(level))
	y_offset=VERT/int(math.sqrt(level))
	button_width=50
	button_height=50
	#display button grid
	for i in range (0,int(math.sqrt(level))):
		for j in range (0,int(math.sqrt(level))):
			newButton=Button(id_count,my_screen,x_offset,y_offset,button_width,button_height)
			id_count+=1
			myButtons.append(newButton)
			x_offset+=button_width+20
		y_offset+=button_height+20
		x_offset=HORIZ/int(math.sqrt(level))
	
	#start the game loop and listen for mouseclicks and mouseovers
	i=0
	dt = pygame.time.get_ticks()
	time_elapsed=0
	max_time=4000+700*pattern_num
	while i<pattern_num and time_elapsed<max_time:
		dt2=pygame.time.get_ticks()
		time_elapsed+=dt2-dt
		dt=dt2
		for ev in pygame.event.get():
			if ev.type==QUIT:
				pygame.quit()
				sys.exit()
			if ev.type==KEYDOWN:
				if ev.key == K_ESCAPE:
					pygame.quit()
					sys.exit()		
			if ev.type==MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					if checkpressed(myButtons, pygame.mouse.get_pos()):
						i+=1
			checkmouseovers(myButtons,pygame.mouse.get_pos())
		pygame.display.update()
		display_time(my_screen,time_elapsed,max_time)

	return myButtons
