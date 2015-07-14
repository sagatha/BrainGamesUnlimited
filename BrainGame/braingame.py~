#
# Python/Braingame
# 
#
# gicharal
#=====================================================


import pygame, sys, random
from pygame.locals import *
from pygame.sprite import *

pygame.init()

# ΚΛΑΣΣΕΙΣ

# Θέση στην οθώνη στην οποία μπορεί να τοπο8ετη8εί κάποια απο τις εικόνες
class Tile(Sprite):
    def __init__(self, createX, createY, dimX, dimY):
        Sprite.__init__(self)
        self.rect = pygame.Rect(createX, createY, dimX, dimY)
        self.isEmpty = True
        self.image = None
        self.itemID = None
        

    def empty(self):
        self.isEmpty = True
        self.itemID = None
        self.image = None
        
        

    def load(self, item, surf):
        if item.isVisible:
            self.itemID = item.id
            self.image = pygame.image.load(str(item.image)+'.jpg')
            self.isEmpty = False
            self.transimage = pygame.transform.scale\
                              (self.image, (self.rect.width, self.rect.height))
            surf.blit(self.transimage, self.rect)
            
#Συλλογή για τη διαχήρηση των αντικειμένων Tile
class Board(Group):
    
    def __init__(self):
        Group.__init__(self)    
               
    def clearBoard(self, screen):
        for myTile in self:
            myTile.empty()
        screen.fill(color)
    #Αλάζει τις εικόνες στην οθώνη κα8ώς και τις θέσεις αυτών         
    def refreshBoard(self, visibleItems, score, itemList, screen):
        self.clearBoard(screen)
        
        #Αντικείμενα που επιλεχτηκαν πιο πριν εμφανίζονται παντα στην οθώνη
        for item in itemList:
            if not item.previouslyPicked:
                item.isVisible = False
            else:
                item.isVisible = True
        
        i=0
        areVisible = score
        if score<23:
            while areVisible < visibleItems:
                if itemList[i].isVisible == False:
                    itemList[i].isVisible = True
                    areVisible +=1
                i += 1
        else:
            for item in itemList:
                item.isVisible = True
        random.shuffle(itemList)

        i = 0
        for myTile in myBoard:
            if itemList[i].isVisible or itemList[i].previouslyPicked:
                myTile.load(itemList[i], my_screen)
            i +=  1

    #Διαχηρείζεται τις τερματικες συνθήκες
    def endGame(self, why, score, screen):
        self.clearBoard(screen)
        text = why+'    '+'Score:'+str(score)
        
        
        while True:

            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.quit()           
                    sys.exit()
                if ev.type == KEYDOWN:
                    pygame.quit()           
                    sys.exit()
                if ev.type == MOUSEBUTTONDOWN:
                    pygame.quit()           
                    sys.exit()
            
            my_font = pygame.font.SysFont(None, 64)
            my_text = my_font.render(text, True, BLACK, WHITE)
            screen.blit(my_text, (20,20))

            my_text = my_font.render("(Press any key to exit)",\
                                     True, BLACK, WHITE)
            screen.blit(my_text, (20,100))
            pygame.display.update()

    
        

#Αντικείμενα οικόνας
class Item(Sprite):
    def __init__(self, identity, image):
        self.id = identity
        self.image = image
        self.previouslyPicked = False
        self.isVisible = False

# Ανάλυση

horiz = 800
vert = 600

# Οθόνη

my_screen = pygame.display.set_mode((horiz, vert), 0, 32)
pygame.display.set_caption('Braingame')

WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
color = WHITE
my_screen.fill(color)
    
pygame.display.update()
# Οδηγίες για το παιχνιδι
#

x = True
while x:

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()           
            sys.exit()
        if ev.type == KEYDOWN:
            x = False
        if ev.type == MOUSEBUTTONDOWN:
            x = False
    my_font = pygame.font.SysFont(None, 64)
    my_text = my_font.render("Don't press the same picture twice",\
                             True, BLACK, WHITE)
    my_screen.blit(my_text, (20,20))

    my_text = my_font.render("(Press any key to continue)",\
                             True, BLACK, WHITE)
    my_screen.blit(my_text, (20,100))
    pygame.display.update()
    
#Εναρξη του παιχνιδιού
#Αρχικοποίηση τιμών
my_screen.fill(color)

myBoard = Board()

for x in range(0,5):
    for y in range(0,5):
        myTile = Tile(x*(horiz/5), y*(vert/5), horiz/5, vert/5)
        myBoard.add(myTile)

itemList =[]

for i in range(0,25):
    myItem = Item(i+1,str(i+1))
    itemList.append(myItem)#Λίστα για τη διαχήρηση των εικόνων

visibleItems = 3    #μεταβλητη που κρατάει το πλή8ος των εικόνων που εμφανίζονται
                    #στην οθώνη
score = 0           #Μεταβλητή που κρατάει το σκορ

#Αρχικά εμφανίζουμε τυχαία 3 αντικείμενα 
random.shuffle(itemList)
for i in range(0,3):
    itemList[i].isVisible = True
random.shuffle(itemList)

i = 0
for myTile in myBoard:
    if itemList[i].isVisible:
        myTile.load(itemList[i], my_screen)
    i +=  1
#
#
#
#
#

pygame.display.update() # Ενημέρωση Video-RAM



while True:
    # ΟΥΡΑ ΓΕΓΟΝΟΤΩΝ: Έλεγχος 
    
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()           
            sys.exit()
            
        # ΚΑΘΟΡΙΣΜΟΣ ΚΑΤΑΣΤΑΣΗΣ
        # 
        if ev.type == KEYDOWN:       
            if ev.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        #Ελεγχουμε αν πατήθηκε καποια απο τις εικόνες
        if ev.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                my_mouse = pygame.mouse.get_pos()
                for myTile in myBoard:
                    if myTile.rect.collidepoint(my_mouse):
                        if not myTile.isEmpty:
                            #Ελέγχουμε αν η  εικονα εχει ξαναεπιλεγεί
                            for item in itemList:
                                if item.id == myTile.itemID and \
                                   item.previouslyPicked:
                                    
                                    myBoard.endGame('You Lost',score, my_screen)
                                    
                                elif item.id == myTile.itemID and \
                                   not item.previouslyPicked:
                                    
                                    item.previouslyPicked = True
                                    visibleItems += 1
                                    score += 1
                                    
                                    if score == 25:
                                        myBoard.endGame('You Won', score, my_screen)
                                    myBoard.refreshBoard(visibleItems,score,\
                                                         itemList,my_screen)
                                
                                              
    pygame.display.update() # Ενημέρωση Video-RAM

