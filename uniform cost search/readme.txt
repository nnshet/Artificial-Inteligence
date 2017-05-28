Name : Neha Shet 
UTA Id: 1001387307
Programming language used : Python

Structure of Program :

	I have created 3 classes :
	1)Reading the file input and storing in the 2 dimensional dictionary as graph.
	2)Priority Queue - Storing each node being processed and assing costs for each nodes.
	3)Ucs - Implements the uniform cost search algorithm for finding the optimal path.

	Program starts by readig the command line arguments
	Program reads the input data from the specified file and the stored the data in the data structure Dictionary.
	Initially, the source node is inserted in the Priority queue and the tracepath function is called.
	In traceroute function of Ucs class 
		1) checks if the queue is empty which checks if the destination is reachable, if the queue is empty it means that the destionation is not rechable.
		2) selects the node from the priorityqueue having the least cost. It does a goal test whether the destination is reached.
		3) It then expands the children for the current node and finds the path cost till each of its child node and inserts in the queue
		4) If the destination is reached it prints out the cost and the path followed from the source to destination

Command for executing program through command prompt:
	python find_route.py input_file.txt source_node destination_node



