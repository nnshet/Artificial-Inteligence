from copy import copy
from copy import deepcopy
import random
import sys

class maxConnect4Game:
    class Node:
        def __init__(self, state):
            self.state = state
            self.children = [None] * 7
            self.parent = None
            self.last_column_changed = None           

        def checkLeafNodes(self):
            
            for elem in self.children:
                if elem is not None:
                    return True
            return False

        def evaluation(self, currentTurn):

            points = 0
            
            mark_1 = currentTurn
	    if currentTurn == 1:
		mark_2 = currentTurn + 1 
	    else: 
		mark_2 = currentTurn - 1

            # horizontal check if there is continous 3's or 2's and 1's
            for row in self.state:

                for begin in range(4):
		    
                    end = begin + 3
                    if row[begin:end] == [mark_1] * 4:
                        points += 1000
                    if row[begin:end-1] == [mark_1] * 3 and row[end-1] == [0]:
                        points += 400
                    if row[begin] == [0] and row[begin+1:end-1] == [mark_1]:
                        points += 400

                    if row[begin:end-2] == [mark_1] * 2 and row[begin+2:end] == [0] * 2:
                        points += 200
                    if row[begin] == [0] and row[begin+1:end-1] == [0] * 2 and row[end-1] == [0]:
                        points += 200
                    if row[begin:end-2] == [0] * 2 and row[begin+2:end] == [mark_1] * 2:
                        points += 200

                    if row[begin:end] == [mark_2] * 4:
                        points -= 1000


            # vertical check if there is continous 3's or 2's and 1's
            for column in range(7):
	    	for row in range(3):
			row1 = row;
			row2 = row +1;
			row3 = row +2;
			row4 = row +3;
                    	if (self.state[row1][column] == mark_1 and self.state[row2][column] == mark_1 and
                        	self.state[row3][column] == mark_1 and self.state[row4][column] == mark_1):
                        	points += 1000
                   	if (self.state[row1][column] == mark_1 and self.state[row2][column] == mark_1 and
                        	self.state[row3][column] == mark_1 and self.state[row4][column] == 0):
                        	points += 400
                    	if (self.state[row1][column] == 0 and self.state[row2][column] == mark_1
                    	    and self.state[row3][column] == mark_1 and self.state[row4][column] == mark_1):
                       		points += 400

                   	if (self.state[row1][column] == mark_1 and self.state[row2][column] == mark_1 and
                    	    self.state[row3][column] == 0 and self.state[row4][column] == 0):
                    		points += 200
                   	if (self.state[row1][column] == mark_1 and self.state[row2][column] == 0 and
                   	     self.state[row3][column] == 0 and self.state[row4][column] == mark_1):
                    	        points += 200
                    	if (self.state[row1][column] == 0 and self.state[row2][column] == mark_1 and
                            self.state[row3][column] == mark_1 and self.state[row4][column] == 0):
                        	points += 200
                   	if (self.state[row1][column] == 0 and self.state[row2][column] == mark_1 and
                        self.state[row3][column] == mark_1 and self.state[row4][column] == 0):
                        	points += 200


                    	if (self.state[row1][column] == mark_2 and self.state[row2][column] == mark_2 and
                        self.state[row3][column] == mark_2 and self.state[row4][column] == mark_2):
                        	points -= 1000


            # Check diagonally
            
	    for col in range(4):
		for row in range(3):
		    row1 = row
		    row2 = row + 1
		    row3 = row + 2
		    row4 = row + 3

		    col1 = col
		    col2 = col + 1
		    col3 = col + 2
		    col4 = col + 3				
                    if (self.state[row1][col1] == mark_1 and self.state[row2][col2] == mark_1 and
                        self.state[row3][col3] == mark_1 and self.state[row4][col4] == mark_1):
                        points += 1000
                    if (self.state[row1][col1] == mark_1 and self.state[row2][col2] == mark_1 and
                        self.state[row3][col3] == mark_1 and self.state[row4][col4] == 0):
                        points += 400
                    if (self.state[row1][col1] == 0 and self.state[row2][col2] == mark_1 and
                        self.state[row3][col3] == mark_1 and self.state[row4][col4] == mark_1):
                        points += 400

                    if (self.state[row1][col1] == mark_2 and self.state[row2][col2] == mark_2 and
                        self.state[row3][col3] == mark_2 and self.state[row4][col4] == mark_2):
                        points -= 1000

            return points
            
        
        
    def __init__(self, depth = 3):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.gameFile = None
        self.depth = depth
        self.branchingFactor = 7
        random.seed()

    # Count the number of pieces already played
    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.gameBoard for piece in row if piece)
        
    # Count the number of playable column
    def checkEmptyColumns(self):
        self.emptyColumns = [index for index, column in enumerate(self.gameBoard[0]) if column == 0]

    # Output current game status to console
    def printGameBoard(self):
        print ' -----------------'
        for i in range(6):
            print ' |',
            for j in range(7):
                print('%d' % self.gameBoard[i][j]),
            print '| '
        print ' -----------------'

    # Output current game status to file
    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        
	if self.currentTurn == 1:
		self.currentTurn = self.currentTurn+1
	else:
		self.currentTurn = self.currentTurn-1
        self.gameFile.write('%s\r\n' % str(self.currentTurn))

    # Place the current player's piece in the requested column
    def playPiece(self, column):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
               
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.currentTurn
                    self.pieceCount += 1
                    return 1
 
    # Construct board state from given board state and column input
    def constructState(self, column, game_state_parent, currentTurn):
        for row in range(5, -1, -1):
            # Checks if column is playable
            if not game_state_parent[row][column]:
                game_state_parent[row][column] = currentTurn
                return game_state_parent
        return None

    def generateTree(self, startNode, depth, currentTurn):
        nextGameState = deepcopy(startNode.state)        
        num_children = self.branchingFactor;
        column = 3                                          
        
        for num in range(0, num_children):
                nextGameState.append(startNode.state)
                newGameState = self.constructState(column, nextGameState, currentTurn)

                if newGameState:
                    startNode.children[num] = self.Node(newGameState)
                    startNode.children[num].last_column_changed = column
                    startNode.children[num].parent = startNode

                if(column < 6):
                    column = column + 1 
                else:
                    column = 0
          
        if(depth != 0):
            for child in startNode.children:
                if child:
			if currentTurn == 1:
				currentTurn = currentTurn+1	
		 	else:
			 	currentTurn = currentTurn-1
                    	self.generateTree(child, depth-1,
                            currentTurn )


    def alphaBetawithDepthLimited(self, node, depth, alpha, beta, maximizingPlayer):

        if(depth == 0 or not node.checkLeafNodes()):
            return node.evaluation(self.currentTurn), node.last_column_changed
    
        if maximizingPlayer:
            minValue = float('-inf')
            column = None

            for childNodes in node.children:
                if childNodes:
                    val, last_column_changed = self.alphaBetawithDepthLimited(childNodes, depth-1, alpha, beta, False)
                    tmp = minValue
                    minValue = max(minValue, val)

                    if minValue != tmp and node.parent:
                        column = node.last_column_changed
                    elif minValue != tmp:
                        column = last_column_changed

                    if minValue >= beta:
                        return minValue, column

                    alpha = max(alpha, minValue)

            return minValue, column
        else:
            minValue = float('inf')
            column = None

            for childNodes in node.children:
                if childNodes:
                    val, last_column_changed = self.alphaBetawithDepthLimited(childNodes, depth-1, alpha, beta, True)
                    tmp = minValue
                    minValue = min(minValue, val)

                    if minValue != tmp and node.parent:
                        column = node.last_column_changed
                    elif minValue != tmp:
                        column = last_column_changed

                    if minValue <= alpha:
                        return minValue, column
                    beta = min(beta, minValue)
            return minValue, column


    def aiPlay(self):
        
        startNode = self.Node(self.gameBoard)
        self.generateTree(startNode, self.depth, self.currentTurn)
        val, column = self.alphaBetawithDepthLimited(startNode, self.depth, float('-inf'), float('inf'), True)
        # maximizingPlayer True because computer first, False otherwise
        self.constructState(column, self.gameBoard, self.currentTurn)
        return column

    # Calculate the number of 4-in-a-row each player has
    def countScore(self):
        self.player1Score = 0;
        self.player2Score = 0;

        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [1]*4:
                self.player1Score += 1
            if row[1:5] == [1]*4:
                self.player1Score += 1
            if row[2:6] == [1]*4:
                self.player1Score += 1
            if row[3:7] == [1]*4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == [2]*4:
                self.player2Score += 1
            if row[1:5] == [2]*4:
                self.player2Score += 1
            if row[2:6] == [2]*4:
                self.player2Score += 1
            if row[3:7] == [2]*4:
                self.player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                   self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                   self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                   self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                self.player1Score += 1
            # Check player 2
            if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                   self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                   self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                   self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
            self.player1Score += 1

        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1

        # Check player 2
        if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
            self.player2Score += 1

        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1