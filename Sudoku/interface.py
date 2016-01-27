import pygame, pygame.font
import os, sys
import sudoku

'''
Graphical User Interface by: alcmenem
Event Handling by: AlexKasapis
'''

def main():
        '''Declaration :
        The border lines are 5 pixels each. Each block is 30x30 and each line is 2 pixel wide.
        The area containing the NewGame and Reset buttons has 30 pixels height.
        This numbers are the ones used when we use specific methods as you can see reading
        through the code.
         
        '''
        pygame.init()

        # Define colors for easier usage
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 153, 0)
        RED = (193, 0, 0)
        GRAY = (112, 138, 144)
        SAND = (240, 240, 230)

        # Create a font
        fontObj = pygame.font.Font("PTC55F.ttf", 18)
        fontObj.set_bold(True)

        #The width and height of the game window
        xAxis = 294
        yAxis = 324

        gameWindow = pygame.display.set_mode((xAxis,yAxis))
        pygame.display.set_caption("SudokuGame")
        gameWindow.fill(SAND)

        # Create the Buttons (NewGame/Reset)
        newLabel = fontObj.render("New Game", 1, BLACK)
        resetLabel = fontObj.render("Reset", 1, BLACK)
        pygame.draw.line(gameWindow, BLACK, (147,1), (147,30), 4)
        gameWindow.blit(newLabel, (25,5))
        gameWindow.blit(resetLabel, (190,5))

        # Create the Borders
        # Horizontal Borders
        pygame.draw.line(gameWindow, BLACK, (0,1), (yAxis-1,1), 4)
        pygame.draw.line(gameWindow, BLACK, (0,yAxis-3), (xAxis,yAxis-3), 4)
        pygame.draw.line(gameWindow, BLACK, (0,30), (yAxis-1,30), 4)
        # Vertical Borders
        pygame.draw.line(gameWindow, BLACK, (xAxis-3,1), (xAxis-3,yAxis), 4)
        pygame.draw.line(gameWindow, BLACK, (1,0), (1,yAxis-1), 4)

        # Block size is 30x30px; line size is 2px
        # Draw the lines (every 32px starting from 34)
        for x in range(34, xAxis, 32):
                pygame.draw.line(gameWindow, BLACK, (x,30), (x,yAxis), 2)
        for y in range(64, yAxis, 32):
                pygame.draw.line(gameWindow, BLACK, (0,y), (xAxis,y), 2)

        # Create and add the number labels to the grid
        startingTable = sudoku.prepareSudokuTable(30) #This array will not change unless the user starts a new game
        gameTable = [[startingTable[row][col] for col in range(9)] for row in range(9)] #This array stores the info about the current game
        for row in range(9): #Add the starting numbers to the grid
                for col in range(9):
                        if startingTable[row][col] != 0:
                                label = fontObj.render(str(gameTable[row][col]), 1, BLACK)
                                gameWindow.blit(label, (col*32+13,row*32+38))

        pygame.display.update()

        gameExit = False
        rowToChange = colToChange = -1

        while not gameExit:
            for event in pygame.event.get():
                #EXIT EVENTS
                if event.type == pygame.QUIT:
                    gameExit = True
                #MOUSE EVENTS
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #Check if the User clicked on a block to change its number
                    if event.button == 1 or event.button == 3:
                        colToChange = (pygame.mouse.get_pos()[0]-5)/32 #Calculate which row and column on the grid did the User click
                        rowToChange = (pygame.mouse.get_pos()[1]-35)/32
                        if event.button == 3: #If the User right clicked, remove the number from the grid, by drawing a rect in front of the number
                            if startingTable[rowToChange][colToChange]==0:
                                pygame.draw.rect(gameWindow, SAND, (colToChange*32+5, rowToChange*32+35, 28, 28), 0)
                                rowToChange = colToChange = -1
                    #Check if the User clicked on the NewGame/Reset Buttons
                    if rowToChange==-1 and colToChange>=0 and colToChange<=3:
                        startingTable = sudoku.prepareSudokuTable(30) #Reset the starting table, the game table, and the grid
                        gameTable = [[startingTable[row][col] for col in range(9)] for row in range(9)]
                        for row in range(9):
                            for col in range(9):
                                    pygame.draw.rect(gameWindow, SAND, (col*32+5, row*32+35, 28, 28), 0)
                                    if startingTable[row][col] != 0:
                                            label = fontObj.render(str(gameTable[row][col]), 1, BLACK)
                                            gameWindow.blit(label, (col*32+13,row*32+38))
                    elif rowToChange==-1 and colToChange>=5 and colToChange<=8:
                        gameTable = [[startingTable[row][col] for col in range(9)] for row in range(9)] #Reset only the game table and the numbers added by the player
                        for row in range(9):
                            for col in range(9):
                                    if startingTable[row][col] == 0:
                                            pygame.draw.rect(gameWindow, SAND, (col*32+5, row*32+35, 28, 28), 0)
                #KEYBOARD EVENTS
                elif event.type == pygame.KEYDOWN:
                    # If the user has clicked on a block to change the number AND this block was empty in the start AND the input is a number
                    if rowToChange!=-1 and colToChange!=-1 and startingTable[rowToChange][colToChange]==0 and event.unicode.isdigit()==True and event.unicode!="0":
                        gameTable[rowToChange][colToChange] = event.unicode #Update the gameTable
                        pygame.draw.rect(gameWindow, SAND, (colToChange*32+5, rowToChange*32+35, 28, 28), 0) #Cover the previous(possibly) number added by the User
                        label = fontObj.render(str(gameTable[rowToChange][colToChange]), 1, GREEN) #Create and all the new number
                        gameWindow.blit(label, (colToChange*32+13,rowToChange*32+38))
                        rowToChange = colToChange = -1
                pygame.display.update()

        pygame.quit()
        quit()

if __name__ == '__main__': main()
