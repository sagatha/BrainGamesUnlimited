# Author Tsesmetzis Prokopis

import simplegui
import random
import time

cardList = []
numOfExposed = 0
firstCard = []
clicks = 0
found = 0
start = 0
end = 0
bestTime = 0

# Creates new game for the first and any next time
#initializing the variables needed
#cardList gets filled with cards from 0 to 7 twice
#and is shuffled
def new_game():
    global cardList, numOfExposed, clicks , start
    start = time.time()
    cardList = []
    numOfExposed = 0
    clicks = 0
    click.set_text("Clicks = 0")
    for i in range(8):
        cardList.append([i,"Grey", "Grey"])
        random.shuffle(cardList)
    for i in range(8):
        cardList.append([i,"Grey", "Grey"])
        random.shuffle(cardList)
    random.shuffle(cardList)
    
#With the mouse position as argument this function enebles the player
#to "click" a card and open it .If there are two cards opened it 
#checks if they match
def mouseclick(pos):
    global numOfExposed, firstCard, clicks , found ,start , end , bestTime
    
    #if two cards are open and they didnt match it hides them
    if numOfExposed == 2:
        for i in range(len(cardList)):
            if cardList[i][2] != "White":
                cardList[i][1] = "Grey"
                cardList[i][2] = "Grey"
                numOfExposed = 0
    
    #top row
    for i in range(len(cardList)/2):
        	
            #only responds to clicks on top row
            if pos[0] > (i*50) and pos[0] < (i*50+50) and pos[1] > 0 and pos[1] < 100 and (cardList[i][1] == "Grey"):
                cardList[i][1] = "Black"
                cardList[i][2] = "Green"
                numOfExposed += 1
            
            	#if one card is exposed store its value 
                if numOfExposed % 2 == 1:
                    firstCard = cardList[i]
                #if two cards are exposed check if they match
                elif numOfExposed % 2 == 0:
                    #if they match make them permantly visible
                    if cardList[i][0] == firstCard[0]:
                        cardList[i][2] = "White"
                        firstCard[2] = "White"
                        numOfExposed = 0
                        found += 1
                    clicks +=2
                    click.set_text("Clicks = " + str(clicks))
    
    #bottom row
    for i in range(len(cardList)/2):
        	
            #only responds to clicks on bottom row
            if pos[0] > (i*50) and pos[0] < (i*50+50) and pos[1] > 100 and pos[1] < 200 and (cardList[i+len(cardList)/2][1] == "Grey"):
                cardList[i+len(cardList)/2][1] = "Black"
                cardList[i+len(cardList)/2][2] = "Green"
                numOfExposed += 1
                
            	#if one card is exposed store its value 
                if numOfExposed % 2 == 1:
                    firstCard = cardList[i+len(cardList)/2]
                #if two cards are exposed check if they match
                elif numOfExposed % 2 == 0:
                    #if they match make them permantly visible
                    if cardList[i+len(cardList)/2][0] == firstCard[0]:
                        cardList[i+len(cardList)/2][2] = "White"
                        firstCard[2] = "White"
                        numOfExposed = 0
                        found += 1
                    clicks +=2
                    click.set_text("Clicks = " + str(clicks))
    
    #checks if all cards are found meaning the game is over
    if found == len(cardList)/2 :
        end = time.time()
        #finds best time of all tries
        if bestTime == 0:
            bestTime = int(end-start)
            secs.set_text("Best time = " + str(int(end-start)) + " sec")
        elif bestTime >= int(end-start):
            bestTime = int(end-start)
            secs.set_text("Best time = " + str(int(end-start))+ " sec")
        found = 0
        start = 0
        end = 0
                    
                    
#Creates the grid with the IDs hidden from the polygons
#Cards and polygons have the same colour at first so the ID
# is not visible
def grid(canvas):    
    
    #drawing the polygons of the top row
    for i in range(len(cardList)/2):
        canvas.draw_polygon([(i*50,0),(i*50+100,0),(i*50+50,100),(i*50,100)],1, "White", cardList[i][1])
        
    #drawing the polygons of the bottom row
        canvas.draw_polygon([(i*50,100),(i*50+100,100),(i*50+50,200),(i*50,200)],1, "White", cardList[i+len(cardList)/2][1])
    
    #drawing the cards numbers of the top row
    for i in range(len(cardList)/2):
        canvas.draw_text(str(cardList[i][0]), (50*i+15,65), 50, cardList[i][2])
        
    #drawing the cards numbers of the bottom row    
    for j in xrange(len(cardList)/2,):
        canvas.draw_text(str(cardList[j+(len(cardList)/2)][0]), (50*j+15,165), 50, cardList[j+(len(cardList)/2)][2])     
    
    
#Creating frame and its buttons and labels
frame = simplegui.create_frame("CARD GAME", 400, 200)
frame.add_button("New game", new_game)
secs=frame.add_label("Best time = 0")
click=frame.add_label("Clicks = 0")


#Start the game for the first time
new_game()
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(grid)
frame.start()