Name: Neha Shet
UTA ID: 1001387308
Programming Language: Python

How the Code is Structure:

The Program has two files:

1) MaxConnect4Game :
	This class is responsible for performing alpha beta pruning algorithm with depth limited search.
2) maxconnect4
	This class contains the main function, reads the command line arguments and plays the game in interactive or one move mode.

MaxConnect4Game has following APIs
 	
	1) constructState: This function is responsible for constructing the game board state with the given column as the input
	2) generateTree:   This function generates a search tree from the start node to its successors till the depth specified.This is used the number of moves in advance that the computer should consider while searching for its next move 
	3) alphaBetawithDepthLimited: This function calculates the minimum and the maximum value for the minimizing player and the maximizing player respectively.
	4) countScore: Counts the score for each of the player.
	5) printGameBoard: Output current game status to console
	6) printGameBoardToFile:Output current game status to the file
	7) evaluation: This function assigns a value to each of the node in the search tree depending on how close the move to this node is towards the winning.

maxconnect4 has following APIs
	1) oneMoveGame: This function is called for making a single move in the game.
	2) makeHumanMove: This function takes input from user and makes the next move for human player
	3) interactiveGame: This function makes computer and the human moves alternatly until the board is full in case of interactive mode .
Instructions to run the program :
 1) Interactive Mode
	
	python maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]
	For Example:
	
	python maxconnect4.py interactive input1.txt computer-next 5
		
2) OneMove Mode
	python maxconnect4.py one-move [input_file] [output_file] [depth]
	For example:

	python maxconnect4.py one-move input1.txt output1.txt 5


