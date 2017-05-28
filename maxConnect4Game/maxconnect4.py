import sys
from MaxConnect4Game import *

def printOutput(currentGame,turn,gameMode):

    if currentGame.player1Score > currentGame.player2Score:
            if gameMode == "interactive":
                if turn == "human-next":
                    print 'You win'
                else:
                    print "You loose. Player 1 has won"
            else:
                print "Player 1 is the winner"
    elif currentGame.player1Score < currentGame.player2Score:
            if gameMode == "interactive":
                if turn == "human-next":
                    print 'You loose. Player 2 has won '
                else:
                    print "You win"
            else:
                print "Player 2 is the winner"
    else:
            print 'Game Drawn'
    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()
    

def oneMoveGame(currentGame,turn,gamemode):

    currentGame.checkPieceCount()
    
    if currentGame.pieceCount == 42:    # Is the board full already?

        print 'BOARD IS FULL\n\nGame Finished!!!!!!!\n'
        currentGame.countScore()
        printOutput(currentGame,turn,gamemode)   
        sys.exit(0)
    
    column = currentGame.aiPlay() + 1 
    print('Game state after move: ')
    currentGame.printGameBoard()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' %(currentGame.player1Score, currentGame.player2Score))
    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()

def makeHumanMove(currentGame,turn,gamemode):

    currentGame.checkPieceCount()
    
    if currentGame.pieceCount == 42:    # Is the board full already?

        print 'BOARD IS FULL\n\nGame Finished!!!!!!!\n'
        currentGame.countScore()
        printOutput(currentGame,turn,gamemode)
        sys.exit(0)

    while True:
        column = int(raw_input('Enter your next move: ')) - 1
        currentGame.checkEmptyColumns()
        if(column in currentGame.emptyColumns):
            break
        else:
            print("Enter a valid column position")
    
    currentGame.constructState(column, currentGame.gameBoard, currentGame.currentTurn)

    print('Game state after move: column', column+1)
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' %(currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()

def interactiveGame(currentGame, outputFile,depthLimit,gameMode, turn = 'computer-next'):
    
    if(turn == 'computer-next'):
        
        oneMoveGame(currentGame,turn,gameMode)
        
        while True:
            currentGame.checkPieceCount()
            print "Moves so far:",currentGame.pieceCount
            del currentGame
            currentGame = maxConnect4Game(depthLimit)
            currentGame.gameFile = open(outputFile, 'r')
            
            file_lines = currentGame.gameFile.readlines()
            currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
            currentGame.currentTurn = int(file_lines[-1][0])
            currentGame.gameFile.close()
            outFile = 'human.txt'
            currentGame.gameFile = open(outputFile, 'w')
            makeHumanMove(currentGame,turn,gameMode)

            currentGame.checkPieceCount()
            print "Moves so far:",currentGame.pieceCount

            del currentGame
            currentGame = maxConnect4Game(depthLimit)
            currentGame.gameFile = open(outputFile, 'r')
            file_lines = currentGame.gameFile.readlines()
            currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
            currentGame.currentTurn = int(file_lines[-1][0])
            currentGame.gameFile.close()

            outFile = 'computer.txt'
            currentGame.gameFile = open(outputFile, 'w')
            oneMoveGame(currentGame,turn,gameMode)
    else:
        
        makeHumanMove(currentGame,turn,gameMode)

        while True:
            currentGame.checkPieceCount()

            print("Moves so far:", currentGame.pieceCount)
            del currentGame

            currentGame = maxConnect4Game(depthLimit)
            currentGame.gameFile = open(outputFile, 'r')
            file_lines = currentGame.gameFile.readlines()
            currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
            currentGame.currentTurn = int(file_lines[-1][0])
            currentGame.gameFile.close()

            outFile = 'computer.txt'
            currentGame.gameFile = open(outputFile, 'w')
            oneMoveGame(currentGame,turn,gameMode)
            currentGame.checkPieceCount()

            print "Moves so far:",currentGame.pieceCount
            del currentGame

            currentGame = maxConnect4Game(depthLimit)
            currentGame.gameFile = open(outputFile, 'r')
            file_lines = currentGame.gameFile.readlines()
            currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
            currentGame.currentTurn = int(file_lines[-1][0])
            currentGame.gameFile.close()

            outFile = 'human.txt'
            currentGame.gameFile = open(outputFile, 'w')
            makeHumanMove(currentGame,turn,gameMode)

def main(argv):
    
    if(len(argv) != 5):
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' %argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' %argv[0]);
        sys.exit(2)	
    game_mode = argv[1]
    
    if(game_mode not in('interactive', 'one-move')):
        print('%s is an unrecognized game mode' %game_mode)
        sys.exit()
    if(game_mode == 'interactive'):
        inFile,turn = argv[2:4]
        if inFile == 'computer-next' or inFile == 'human-next':
            depth = turn
            turn = inFile
            inFile = None
        else:
            depth = argv[4]    
    elif(game_mode == 'one-move'):
         inFile, outFile, depth = argv[2:5]

    depth = int(depth)
    currentGame = maxConnect4Game(depth) 

    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if turn == 'computer-next':
            outFile = 'computer.txt'
        else:
            outFile = 'human.txt'
    
        currentGame.gameFile = open(outFile, 'w')
        interactiveGame(currentGame, outFile, depth, game_mode, turn)
    else:
        turn = "";
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,turn,game_mode) 

if __name__ == '__main__':
    main(sys.argv)
