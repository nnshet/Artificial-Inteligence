1) Name - Neha Shet
2) UTA ID - 1001387308
3) Programming Language - Python
4) How to run the program:

     	program_name.py [arguments]
	e.g. python bnet.py  Bt Af given Mf
5) How the code is structured?
•	There are 2 files BayesianNetwork.py and bnet.py.
•	BayesianNetwork.py is a class file which contains function computeProbability. 
        It also contains initial probability values stored in a dictionary.
•	The function computeProbability takes six parameters, 
	the boolean values for the five variables namely - burglary, earthquake, alarm, john calling, mary calling 
	and a list of variables that are given as condition.
•	The file bnet.py contains createTableRow which takes an empty list and 
	the list of values for the variables and returns a list of boolean values that represents a row in the truth table for the variables.
•	The main function creates list of boolean values depending on the given input and calls computeProbability function for each table row.
		

     


