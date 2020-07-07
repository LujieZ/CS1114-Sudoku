# Lujie Zhao
# lz1860
# CS-UY 1114
# SEC EXL3
# Jeff Epstein
# Final Project

import turtle
import time
import random
import math

# Global Variables
level = "" # Y for Hard Mode and N for Easy Mode
n = 9 # The length of the grid
length = 30 # The length of the square
maxAttempts = 100 # Stop random generation after 100 attempts
timer = 0 # Time the game for 20 mins
board = [] # A generated answer for the game
location = [] # A list to collect generated board and user input
xIndex = 9 # First index for the location list
yIndex = 9 # Second index for the location list
result = False # If the game is solved correctly

def grid(n,length):
    """
    Sig: int, int -> NoneType
    Take the parameters and make a 9x9 grid in turtle.
    """
    sign = 1
    
    for i in range(2):
        for j in range(n):
            turtle.forward(length * n)
            turtle.left(sign * 90)
            turtle.forward(length)
            turtle.left(sign * 90)
            sign = 0- sign
        # Change the direction of the turtle.
        turtle.forward(length * n)
        turtle.left(90)
        sign = 0 - sign

def drawGrid():
    """
    Sig: NoneType -> NoneType
    Call grid and draw the 9x9 grid in turtle.
    Print out all the instructions.
    """
    # Turn turlte animation off an set delay for update drawings.
    turtle.tracer(0,0)
    # Make the turtle invisible and speed up the drawing.
    turtle.hideturtle()
    
    turtle.clear()
    turtle.setup(700,580)
    turtle.penup()
    turtle.goto(-135,-135)
    turtle.pendown()

    # Call grid.
    grid(n,length)
    
    # Print instructions for the game.
    turtle.penup()
    turtle.goto(-80,215)
    turtle.color("black")
    turtle.write("SUDOKU",True,font=("New York",40,"bold"))
    turtle.goto(-200,190)
    turtle.color("#255359")
    turtle.write("Click on empty squares and enter digits 1 to 9!",True,font=("Lucida Sans Unicode",17,"bold"))
    turtle.goto(-200,172)
    turtle.color("#0089A7")
    turtle.write("- You have a total of 20 minutes",True,font=("Lucida Sans Unicode",15,"normal"))
    turtle.goto(-230,-170)
    turtle.write("Instructions:",True,font=("Lucida Sans Unicode",15,"bold"))
    turtle.goto(-230,-188)
    turtle.color("#255359")
    turtle.write("1. Fill the grid so that each column, each row, and each of the nine",True,font=("Lucida Sans Unicode",15,"normal"))
    turtle.goto(-212,-205)
    turtle.write("3x3 boxes contains digits from 1 to 9.",True,font=("Lucida Sans Unicode",15,"normal"))
    turtle.goto(-230,-222)
    turtle.write("2. To rewrite a square, just reclick on the square and enter the new",True,font=("Lucida Sans Unicode",15,"normal"))
    turtle.goto(-212,-239)
    turtle.write("digit you wish to add.",True,font=("Lucida Sans Unicode",15,"normal"))
    turtle.goto(170,77)
    turtle.color("#AB3B3A")
    turtle.write("Click and ",True,font=("New York",17,"normal"))
    turtle.goto(170,60)
    turtle.write("press space",True,font=("New York",17,"normal"))
    turtle.goto(170,42)
    turtle.write("for hints!",True,font=("New York",17,"normal"))

    # Draw a box for hints instruction.
    turtle.goto(163,100)
    turtle.color("#AB3B3A")
    turtle.pendown()
    turtle.left(90)
    for l in range(2):
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(86)
        turtle.left(90)  
    turtle.update()

def printArray():
    """
    Sig: NoneType -> NoneType
    Print a nested 0 list as the base for the baord.
    """
    board = []
    
    for i in range(9):
        acc = []
        for j in range(9):
            acc.append(0)
        board.append(acc)

    return board
        
def printLocation():
    """
    Sig: NoneType -> NoneType
    Print the numbers for the game.
    """
    global location
    
    turtle.penup()
    turtle.goto(-125,110)
    turtle.color("black")
    for n in range(9):
        for m in range(9):
            turtle.setpos(-125+m*length,110-n*length)
            if location[n][m] != 0:
                turtle.write(str(location[n][m]),True,font=("New York",17,"normal"))
                turtle.penup()
                
    turtle.update()
                
def checkNeighbors(row,col):
    """
    Sig: int, ins -> list(ints)
    Collect all numbers of the current neighbors.
    Use row and col to get the location of the
    current grid.
    """
    global board
    
    subCol = int(col / 3)
    subRow = int(row / 3)
    subGrid = []
    for subR in range(3):
        for subC in range(3):
            subGrid.append(board[subRow*3+subR][subCol*3+subC])
            
    return subGrid
    
def getBoard():
    """
    Sig: NoneType -> NoneType
    Generate a possible solution for a Sudoku game
    by random generation. All the numbers are picked
    randomly with in 1 to 9 while checking their row,
    columns and 3x3 subgrid. The answer is stored in
    the list board.
    """
    global board
    counter = 9999

    while counter > maxAttempts:
        board = printArray()
        for row in range(9):
            for col in range(9):
                # Collect all numbers of the current row
                # All numbers in one row are in the same nested list
                Row = board[row]
                Col = []
                # Collect all numbers of the current column
                for thisRow in range(9):
                    Col.append(board[thisRow][col])
            
                subGrid = checkNeighbors(row,col)
                
                r = 0
                # Reset the counter and start counting
                counter = 0
                # Get random number for a square
                while r in Row or r in Col or r in subGrid:
                    r = random.randint(1,9)
                    counter += 1
                    if counter > maxAttempts:
                        break 
                board[row][col] = r
                
                if counter > maxAttempts:
                    break 
            if counter > maxAttempts:
                break
            
    for number in board: print(number)
    print()

def getLocation(smallest,largest):
    """
    Sig: NoneType -> NoneType
    Random generate the number of digits appear
    on the rows and columns of the board. Use 0
    as a space holder for further checking.
    """
    global location,board
    
    location = printArray()
    for i in range(9):
        n = random.randint(smallest,largest)
        for j in range(n):
            val = random.randint(0,8)
            while location[i][val] != 0:
                val = random.randint(0,8)
            location[i][val] = board[i][val]
            
    for number in location: print(number)
    print()

def getPos(num):
    """
    Sig: int -> int
    Turn the coordinates of the click handler
    into the index of the location list. 
    """
    num = num / 30
    index = -1
    count = -4.5
    
    for i in range(9):
        if count < num and num < (count+1):
            index = i
        count += 1        
    
    return index
    
def getInput(userInput,color):
    """
    Sig: float, float, int -> NoneType
    The user input is put into the location list
    as a negative number. The original board cannot
    be changed during out the game.
    """
    global xIndex,yIndex,location

    if location[yIndex][xIndex] <= 0:
        turtle.setpos(-115+xIndex*length,126-yIndex*length)
        turtle.color("white")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(15)
            turtle.right(90)
        turtle.end_fill()
        turtle.color(color)
        turtle.setpos(-125+xIndex*length,110-yIndex*length)
        turtle.write(str(userInput),True,font=("New York",17,"normal"))
        turtle.update()
        
        location[yIndex][xIndex] = -userInput
    else:
        print("ERROR! Please click on an empty square!")

def genLocation():
    """
    Sig: int, int -> NoneType
    After knowing the hardness level, generate the
    location of the digits. For harder games, there
    are more empty squares on board. For easier games,
    there are fewer squares on board.
    """
    global level
    
    if level == "Y":
        getLocation(2,4)
    if level == "N":
        getLocation(3,6)

def genHints():
    """
    Sig: NoneType -> NoneType
    Show hints for the user. Get the correct value for
    one square from originally generated board and display
    on the game board with a differnt color.
    """
    global board,xIndex,yIndex
    getInput(board[yIndex][xIndex],"#F6C555")
    checkGameOver()
    
def clickHandler(x,y):
    """
    Sig: int, int -> NoneType
    Get the index of the area where the user
    clicked.
    """
    global xIndex,yIndex,location

    xIndex = getPos(x)
    yIndex = getPos(-y)
    if xIndex == -1 or yIndex == -1:
        print("ERROR! Please click an empty square in the board!")
    elif location[yIndex][xIndex] != 0:
        print("ERROR! Please click on an empty square!")
    else:
        print("x index: ",xIndex,"y index: ",yIndex)
   
def keyHandler1():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 1. It puts the -1
    into location list and checks if the user
    has won the game.
    """
    userInput = 1
    getInput(userInput,"#0089A7")
    checkGameOver()

def keyHandler2():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 2. It puts the -2
    into location list and checks if the user
    has won the game.
    """
    userInput = 2
    getInput(userInput,"#0089A7")
    checkGameOver()

def keyHandler3():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 3. It puts the -3
    into location list and checks if the user
    has won the game.
    """
    userInput = 3
    getInput(userInput,"#0089A7")
    checkGameOver()

def keyHandler4():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 4. It puts the -4
    into location list and checks if the user
    has won the game.
    """
    userInput = 4
    getInput(userInput,"#0089A7")
    checkGameOver()

def keyHandler5():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 5. It puts the -5
    into location list and checks if the user
    has won the game.
    """
    userInput = 5
    getInput(userInput,"#0089A7")
    checkGameOver()

def keyHandler6():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 6. It puts the -6
    into location list and checks if the user
    has won the game.
    """
    userInput = 6
    getInput(userInput,"#0089A7")
    checkGameOver()
    
def keyHandler7():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 7. It puts the -7
    into location list and checks if the user
    has won the game.
    """
    userInput = 7
    getInput(userInput,"#0089A7")
    checkGameOver()

def keyHandler8():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 8. It puts the -8
    into location list and checks if the user
    has won the game.
    """
    userInput = 8
    getInput(userInput,"#0089A7")
    checkGameOver()

def keyHandler9():
    """
    Sig: NoneType -> NoneType
    Key handler for digit 9. It puts the -9
    into location list and checks if the user
    has won the game.
    """
    userInput = 9
    getInput(userInput,"#0089A7")
    checkGameOver()

def checkGameOver():
    """
    Sig: NoneType -> NoneType
    It checks if the user has completed the grid
    with correct number digits within the 20 mins
    time limit. All numbers are in absolute values
    so their signs do not matter.
    """
    global location,timer

    result = True
    for row in range(9):
        rSum = 0
        cSum = 0
        for col in range(9):
            gSum = 0
            cSum += abs(location[row][col])
            rSum += abs(location[col][row])
            
            if row == 1 or row == 4 or row == 7:
                if col == 1 or col == 4 or col == 7:
                    for sRow in range(2):
                        for sCol in range(2):
                            gSum += abs(location[col+sRow][row+sCol])
                            
            if location[row][col] == 0 or location[col][row] == 0:
                result = False 
        if gSum != 45 and gSum != 0:
            result = False
    if cSum != 45 and rSum != 45:
        result = False

    if result == True and timer <= 20:
        outcome = "YOU WIN"
        color = "#F6C555"
        gameEnd(outcome,color)
    elif timer > 20:
        outcome = "YOU LOSE"
        color = "#AB3B3A"
        gameEnd(outcome,color)
            
    print(result)

def gameTime():
    """
    Sig: NoneType -> NoneType
    Add number to the timer for the game
    and start counting for the time.
    """
    global timer
    timer += 1
    turtle.ontimer(gameTime, 60000)

def gameError():
    """
    Sig: NoneType -> NoneType
    Define possible errors.
    """
    try:
        location[yIndex][xIndex]
    except IndexError:
        print("ERROR! Please click on empty square in the board!")
        
    try:
        location[n][m]
    except IndexError:
        print("ERROR! Please give a valid input for the game!")
    
def gameEnd(outcome,color):
    """
    Sig: str, str -> NoneType
    Draw a circle to display and write out
    the result.
    """
    turtle.penup()
    turtle.setposition(-83,0)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(87)
    turtle.end_fill()
    turtle.setposition(-41,-12)
    turtle.color("white")
    turtle.write(outcome,True,font=("Lucida Sans Unicode",20,"bold"))
    
    turtle.update()

def gameStart():
    """
    Sig: NoneType -> NoneType
    Starter code for the game.
    """
    drawGrid()
    getBoard()
    genLocation()
    printLocation()

    turtle.onscreenclick(clickHandler)
    turtle.onkey(keyHandler1,"1")
    turtle.onkey(keyHandler2,"2")
    turtle.onkey(keyHandler3,"3")
    turtle.onkey(keyHandler4,"4")
    turtle.onkey(keyHandler5,"5")
    turtle.onkey(keyHandler6,"6")
    turtle.onkey(keyHandler7,"7")
    turtle.onkey(keyHandler8,"8")
    turtle.onkey(keyHandler9,"9")
    turtle.onkey(genHints,"space")
    
    turtle.listen()

def main():
    """
    Sig: NoneType -> NoneType
    Main function for the game.
    """
    global level
    turtle.title("Sudoku - Lujie(Sue) Zhao")
    turtle.bgpic("lz1860_Sudoku_bgpic.gif")
    # Enter Y for Hard Mode and N for Easy Mode
    level = turtle.textinput("Let's choose a hardness level","Are you an expert at Sudoku? ;) (Y/N)")
    gameTime()
    gameError()
    gameStart()
    turtle.mainloop()

main()
