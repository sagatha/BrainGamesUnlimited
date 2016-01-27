import random

'''
Algorithm by: alcmenem
Algorithm implementation: akasapis, alcmenem
'''

def shuffleSet(numberSets, j):
    '''
    Author: akasapis
    Copies the 1st, 2nd or 3rd set of 3 numbers from the first row of the numberSets
    array, swaps twice this small array and returns it.
    For example if:
    1 5 3 | 8 2 9 | 7 6 4
    5 3 1 | 2 9 8 | 6 4 7
    3 1 5 | 9 8 2 | 4 7 6
    is the numberSets and j==1, then tempSet==[8, 2, 9], and after the swaps, it could be
    [2, 9, 8]
    '''
    tempSet = [numberSets[0][z+j*3] for z in range(3)]
    for swapTimes in range(2):
        index1 = random.randint(0, 2)
        index2 = random.randint(0, 2)
        tempCell = tempSet[index1]
        tempSet[index1] = tempSet[index2]
        tempSet[index2] = tempCell
    return tempSet

def checkValidation(numberSets, tempSet, i, j):
    '''
    Author: akasapis
    Gets the numberSets 2D array, the i and j coords to the numberSets and the tempSet and
    checks whether the tempSet and the numberSet combinations are unique. For example the
    combinations can be:
    [2 4 6] but not [2 4 6]
    [6 2 4]         [6 4 2]
    '''
    for y in range(3):
        for x in range(i):
            if tempSet[y] == numberSets[x][y+3*j]:
               return False
    return True

def getNumberSets():
    '''
    Author: akasapis
    Create the 3x9 array filled with the number sets that will be used to fill
    the sudoku table. These will be 3 sets of 3 numbers, in 3 unique combinations.
    Final example can be:
    1 5 3 | 8 2 9 | 7 6 4
    5 3 1 | 2 9 8 | 6 4 7
    3 1 5 | 9 8 2 | 4 7 6
    '''
    # Initialize the array, and fill the first row with 1-9
    numberSets = [[0 for i in range(9)] for i in range(3)]
    for i in range(9):
        numberSets[0][i] = i+1
    # Shuffle the numbers of the first row
    for i in range(20):
        index1 = random.randint(0, 8)
        index2 = random.randint(0, 8)
        tempCell = numberSets[0][index1]
        numberSets[0][index1] = numberSets[0][index2]
        numberSets[0][index2] = tempCell
    # Create the combinations of the sets
    for i in range(2): # Which row
        for j in range(3): # Which combination
            tempSet = shuffleSet(numberSets, j)
            validSet = False
            while validSet == False:
                validSet = checkValidation(numberSets, tempSet, i+1, j)
                if validSet == False:
                    tempSet = shuffleSet(numberSets, j)
            numberSets[i+1][0+3*j] = tempSet[0]
            numberSets[i+1][1+3*j] = tempSet[1]
            numberSets[i+1][2+3*j] = tempSet[2]
    return numberSets

def getSets(numberSets, setsNumber):
    '''
    Author: akasapis
    Gets the numberSets 2D array and which one of the 3 sets of combinations the
    program wants. For example, if:
    1 5 3 | 8 2 9 | 7 6 4
    5 3 1 | 2 9 8 | 6 4 7
    3 1 5 | 9 8 2 | 4 7 6
    is the numberSets and the setsNumber is equal to 1, the return value will be:
    8 2 9
    2 9 8
    9 8 2
    '''
    tempSets = [[0 for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            tempSets[i][j] = numberSets[i][j+3*setsNumber]
    return tempSets

def getEmptyRow(sudokuTable, bigRow):
    '''
    Author: akasapis
    Gets the main sudoku table, which is being filled, and one of the three main rows
    (big block) and returns a random row of that block the is not yet filled with numbers.
    '''
    randRow = random.randint(0, 2)
    while True:
        if sudokuTable[randRow+bigRow*3][0] == 0:
            return randRow
        randRow = (randRow + 1) % 3

def fillTable(sudokuTable, numberSets):
    '''
    Author: akasapis
    Fills the sudoku table with the cycle algorithm.
    '''
    for setsNumber in range(3):
        tempSets = getSets(numberSets, setsNumber)
        for bigRow in range(3):
            startingRow = getEmptyRow(sudokuTable, bigRow)
            for bigCol in range(3):
                sudokuTable[startingRow+bigRow*3][0+bigCol*3] = tempSets[(bigRow+bigCol)%3][0]
                sudokuTable[startingRow+bigRow*3][1+bigCol*3] = tempSets[(bigRow+bigCol)%3][1]
                sudokuTable[startingRow+bigRow*3][2+bigCol*3] = tempSets[(bigRow+bigCol)%3][2]
                startingRow = (startingRow + 1) % 3
    return sudokuTable

def createFullTable():
    '''
    Author: akasapis
    Create the numberSets and initialize the sudoku table, and then call the fillTable method
    to fill the table with the sets.
    '''
    numberSets = getNumberSets()
    sudokuTable = [[0 for i in range(9)] for i in range(9)]
    sudokuTable = fillTable(sudokuTable, numberSets)
    return sudokuTable

def prepareSudokuTable(number):
    '''
    Author: alcmenem
    Get the full table with the createFullTable function and then randomly copy numbers from
    the full table to the empty one.
    '''
    fullTable = createFullTable()
    sudokuTable = [[0 for i in range(9)] for i in range(9)]
    for i in range(number):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if sudokuTable[row][column] == 0:
            sudokuTable[row][column] = fullTable[row][column]
        else:
            while sudokuTable[row][column] != 0:
                 row = random.randint(0, 8)
                 column = random.randint(0, 8)
                 if sudokuTable[row][column] == 0:
                     sudokuTable[row][column] = fullTable[row][column]
                     break
    return sudokuTable

