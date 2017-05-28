Name: Neha Shet
UTA ID: 1001387308
Programming Language: Python

How the Code is Structure:

The program calculates the posterior probabilities and also calculates the prbability of next candy being picked as lime or cherries
The Program has following functions:

The main takes the input from the command line which is the series of observations so far.

The calculatePosteriorHypothesis function calculates the posterior probabilities using the dynamic programming technique and inturn calls the calculateDenominator method to do the calculation according to the formula given in the slide.
At each iteration the probability calculated is placed in the adjacency matrix and the last row will contain all the output values.

Lastly, the result file is created and the values are print to it.

command to run the Program:

python compute_a_posteriori.py observations

For example:
python compute_a_posteriori.py CLLCCLLLCCL
