import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
GRAY = (47, 79, 79)
CORAL = (240, 128, 128)
ORANGE = (255, 165, 0)
BLUE2 = (0, 0, 205)
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Instruction Screen")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5
 
# This is a font we use to draw text on the screen (size 30)
font = pygame.font.Font(None, 30)

 
display_instructions = True
instruction_page = 1
 
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() [0]:
                instruction_page += 1
                if instruction_page == 3:
                     display_instructions = False
            if pygame.mouse.get_pressed() [2]:
                    instruction_page +=2
            if instruction_page == 5:
                display_instructions = False
       
                
 
    # Set the screen background
    screen.fill(GRAY)




 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("ΑΣΚΗΣΗ ΜΝΗΜΗΣ", True, BLUE)
        screen.blit(text, [200, 10])
        text = font.render("Παρατήρησε τα σχήματα και τα χρώματά τους.", True, WHITE)
        screen.blit(text, [10, 40])
        pygame.draw.circle(screen, RED, (250, 150), 40, 0)
        pygame.draw.rect(screen, ORANGE, (200, 250, 150, 100))
        pygame.draw.rect(screen, PURPLE, (200, 380, 100, 100))
        text = font.render("Κάνε αριστερό κλικ για συνέχεια", True, WHITE)
        screen.blit(text, [10, 60])
 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Κάνε αριστερό κλικ αν το σχήμα υπήρχε στην προηγούμενη οθόνη.", True, WHITE)
        screen.blit(text, [10, 40])
        text = font.render("Διαφορετικά κάνε δεξί κλικ.", True, WHITE)
        screen.blit(text, [10, 80])
        pygame.draw.circle(screen, RED, (300, 200), 60, 0)
        
        
    if instruction_page == 3:
        # Draw instructions, page 3
        text = font.render("ΣΩΣΤΟ!!!", True, GREEN)
        screen.blit(text, [300, 200])

    if instruction_page == 4:
        # Draw instructions, page 4
        text = font.render("ΛΑΘΟΣ...", True, GREEN)
        screen.blit(text, [300,200])
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        text = font.render("Σωστό", True, WHITE)
        screen.blit(text, [10, 40])
    # Set the screen background
    screen.fill(GRAY)
 
    

    
    
    
 
    # Limit to 60 frames per second
clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

