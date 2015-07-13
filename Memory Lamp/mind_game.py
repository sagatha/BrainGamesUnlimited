from MyLibrary import *
from random import *

# Εμφάνιση της αρχικής οθόνης
def display_start_screen():
    my_screen.blit(back,screen_rect)
    pygame.draw.rect(my_screen, YELLOW, start_rect, 0)
    pygame.draw.rect(my_screen, YELLOW, quit_rect, 0)
    my_screen.blit(title,(134,50))
    my_screen.blit(start_button,(264,200))
    my_screen.blit(quit_button,(265,280))
    my_screen.blit(start_image_1,(50,185))
    my_screen.blit(start_image_2,(450,185))
    my_screen.blit(start_image_3,(50,265))
    my_screen.blit(start_image_4,(450,265))
    pygame.display.update()

# Εφμάνιση οθόνης οδηγιών
def display_instructions():
    my_screen.blit(back,screen_rect)
    my_screen.blit(choose,(114,50))
    pygame.draw.rect(my_screen, YELLOW, continue_rect, 0)
    my_screen.blit(instructions_image,instructions_rect)
    my_screen.blit(continue_button,(250,330))
    pygame.display.update()

# Εμφάνιση κύριας οθόνης παιχνιδιού
def display_game_screen():
    my_screen.blit(back,screen_rect)
    pygame.draw.rect(my_screen, YELLOW, restart_rect, 0)
    pygame.draw.rect(my_screen, YELLOW, quit_rect_2, 0)
    my_screen.blit(restart_button,(510,15))
    my_screen.blit(quit_button_2,(520,55))
    update_score()
    for i in range(7):
        lamps[i].draw(my_screen)
    pygame.display.update()

# Άναψε τη λάμπα i
def light_ball(i):
    pygame.mixer.music.play()
    lamps[i].make_highlight()
    lamps[i].draw(my_screen)
    pygame.display.update()
    pygame.time.delay(150)
    lamps[i].make_simple()
    lamps[i].draw(my_screen)
    pygame.display.update()

# Ανανέωση σκορ
def update_score():
    score_text = my_font_3.render("Score: "+str(score),True,BLACK)
    my_screen.blit(pygame.image.load("score.png"),score_rect)
    my_screen.blit(score_text,(10,10))
    pygame.display.update()

# Εμφάνιση μηνύματος κατάστασης παιχνιδιού
def show_message(text):
    message = my_font_3.render(text, True,BLACK)
    my_screen.blit(back_message,message_rect)
    my_screen.blit(message,(160,130))
    update_score()
    pygame.display.update()


pygame.init()

# -- MAIN ------------------------
my_clock = pygame.time.Clock()

# (2) ΕΝΑΡΞΗ - SETUP
# Ανάλυση
HORIZ=600
VERT=400

# Οθόνη
my_screen = pygame.display.set_mode((HORIZ, VERT), 0, 32)
pygame.display.set_caption('Memeory Lamp')

screen_rect = pygame.Rect(0, 0, 600, 400)
back = pygame.image.load("background.png")
back_message = pygame.image.load("back_message.png")


# Άλλες ρυθμίσεις
# Χρώματα
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 51)
ORANGE = (255, 153, 0)
BROWN = (153, 0, 0)
LIGHT_BLUE = (135,206,250)


# Αρχική κατάσταση παιχνιδιού
score = 0
state = 1   # Οθόνη που θα εμφανιστεί ανάλογα με την κατάσταση : 1-Αρχική , 2-Οδηγίες, 3-Παιχνίδι, ( 4-Game over )
level = 1
play = False

# Κείμενο
my_font = pygame.font.SysFont(None,64)
my_font_2 = pygame.font.SysFont(None,46)
my_font_3 = pygame.font.SysFont(None,32)

# Τα αντικείμενα που θα εμφανιστούν στις οθόνες
title = my_font.render('MEMORY TEST',True,BLACK)
choose = my_font.render('Choose difficulty',True,BLACK)

start_button = my_font_2.render('Start',True,BLACK)
start_rect = pygame.Rect(225, 193, 150, 40)

start_image_1 = pygame.image.load("lamp4.png")
start_image_2 = pygame.image.load("lamp6.png")
start_image_3 = pygame.image.load("lamp7.png")
start_image_4 = pygame.image.load("lamp2.png")

quit_button = my_font_2.render('Quit',True,BLACK)
quit_rect = pygame.Rect(225, 273, 150, 40)

instructions_image = pygame.image.load("instructions.png")
instructions_rect = pygame.Rect(0, 0, 600, 308)

continue_button = my_font_3.render('Continue',True,BLACK)
continue_rect = pygame.Rect(225, 320, 150, 40)

score_text = my_font_3.render("Score: "+str(score),True,BLACK)
score_rect = pygame.Rect(0, 0, 202, 117)

message_rect = pygame.Rect(0,0,447,202)

restart_button = my_font_3.render('Restart',True,BLACK)
restart_rect = pygame.Rect(500, 10, 100, 30)

quit_button_2 = my_font_3.render('Quit',True,BLACK)
quit_rect_2 = pygame.Rect(500, 50, 100, 30)

# Ο ήχος που θα ακούγεται κατα την εμφάνιση της φωτισμένης λάμπας
pygame.mixer.music.load("lightup.wav")

#  Η λίστα με τις λάμπες που θα εμφανιστούν στην οθόνη παιχνιδιού
lamps = []
lamps.append(Lamp(1,25,200,100,70,"lamp1.png","light1.png",False))
lamps.append(Lamp(2,175,200,100,70,"lamp2.png","light2.png",False))
lamps.append(Lamp(3,325,200,100,70,"lamp3.png","light3.png",False))
lamps.append(Lamp(4,475,200,100,70,"lamp4.png","light4.png",False))
lamps.append(Lamp(5,100,300,100,70,"lamp5.png","light5.png",False))
lamps.append(Lamp(6,250,300,100,70,"lamp6.png","light6.png",False))
lamps.append(Lamp(7,400,300,100,70,"lamp7.png","light7.png",False))

pygame.display.update()




#=========================================================
# (3) ΒΡΟΧΟΣ ΠΑΙΧΝΙΔΙΟΥ

while True:
    if state == 1:
        display_start_screen()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and start_rect.collidepoint(pygame.mouse.get_pos()):
                    state=2
                    pygame.time.delay(300)
                    display_instructions()
                elif pygame.mouse.get_pressed()[0] and quit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()


    elif state == 2:
        display_instructions()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and continue_rect.collidepoint(pygame.mouse.get_pos()):
                    state=3
                    pygame.time.delay(300)
                    display_game_screen()

    elif state == 3:
        # Αρχικοποίηση του κάθε level του παιχνιδιού
        if not play:
            pattern = [randint(0,6) for i in range(level)]
            pygame.time.delay(300)
            show_message("Look carefully !!!")
            pygame.time.delay(700)
            for i in range(level):
                light_ball(pattern[i])
                pygame.time.delay(150)
            pygame.time.delay(600)
            show_message("Go !")
            to_check = 0
            play=True

        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and lamps[0].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==0:
                        score+=10
                        update_score()
                        light_ball(0)
                        to_check += 1
                    else:
                        light_ball(0)
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(700)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[1].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==1:
                        score+=10
                        update_score()
                        light_ball(1)
                        to_check += 1
                    else:
                        light_ball(1)
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(700)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[2].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==2:
                        score+=10
                        update_score()
                        light_ball(2)
                        to_check += 1
                    else:
                        light_ball(2)
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(700)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[3].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==3:
                        score+=10
                        update_score()
                        light_ball(3)
                        to_check += 1
                    else:
                        light_ball(3)
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(700)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[4].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==4:
                        score+=10
                        update_score()
                        light_ball(4)
                        to_check += 1
                    else:
                        light_ball(4)
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(700)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[5].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==5:
                        score+=10
                        update_score()
                        light_ball(5)
                        to_check += 1
                    else:
                        light_ball(5)
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(700)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[6].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==6:
                        score+=10
                        update_score()
                        light_ball(6)
                        to_check += 1
                    else:
                        light_ball(6)
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(700)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and restart_rect.collidepoint(pygame.mouse.get_pos()):
                    state = 3
                    play=0
                    level=1
                    score=0
                elif pygame.mouse.get_pressed()[0] and quit_rect_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if(to_check>=len(pattern)):
                    show_message("Great work!")
                    play=0
                    level += 1
                    pygame.time.delay(300)



            if ev.type == KEYDOWN:

                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    else:
        # Η οθόνη του Game Over επιτρέπει μόνο το πάτημα του κουμπιού Restart και Quit
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and restart_rect.collidepoint(pygame.mouse.get_pos()):
                    state = 3
                    play=0
                    level=1
                    score=0
                elif pygame.mouse.get_pressed()[0] and quit_rect_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()











