import sys;

q_observations = {"Ch1":1.0,"Lh1":0.0,"Ch2":0.75,"Lh2":0.25,"Ch3":0.50,"Lh3":0.50,"Ch4":0.25,"Lh4":0.75,"Ch5":0.0,"Lh5":1.0}
def calculateDenominator(ch,x,posteriorHypothesis):
    
    a = round(q_observations[ch+"h1"]*posteriorHypothesis[x-1][0],5);
    b = round(q_observations[ch+"h2"]*posteriorHypothesis[x-1][1],5);
    c = round(q_observations[ch+"h3"]*posteriorHypothesis[x-1][2],5);
    d = round(q_observations[ch+"h4"]*posteriorHypothesis[x-1][3],5);
    e = round(q_observations[ch+"h5"]*posteriorHypothesis[x-1][4],5);
    return a+b+c+d+e;


def calculatePosteriorHypothesis(observations):
    
    t = len(observations);
    
    posteriorHypothesis = [[0 for j in range(5)] for i in range(t+1)] 
    posteriorHypothesis[0][0]= 0.10;
    posteriorHypothesis[0][1]= 0.20;
    posteriorHypothesis[0][2]= 0.40;
    posteriorHypothesis[0][3]= 0.20;
    posteriorHypothesis[0][4]= 0.10;
    
    for x in range(1,t+1):
        for y in range(5):
            ch = observations[x-1];
           
            q_observations[ch+"h"+str(y+1)]
            d = calculateDenominator(ch,x,posteriorHypothesis);
            posteriorHypothesis[x][y] = round(q_observations[ch+"h"+str(y+1)]*posteriorHypothesis[x-1][y]/d,5);
    return posteriorHypothesis;

def writeOutputToFile(answer,observations):
    
    total_observations = len(observations);
    f = open("result.txt","w");
    f.write("\n Observation sequence Q: "+observations)
    f.write("\n Length of Q: "+str(total_observations)+"\n");
    for s in range(5):
        f.write("\n P(h"+str(s+1)+" | Q) = "+str(answer[total_observations][s]));
    f.write("\n\n Probability that the next candy we pick will be C, given Q: "+str(calculateDenominator('C',total_observations-1,answer)));
    f.write("\n Probability that the next candy we pick will be L, given Q: "+str(calculateDenominator('L',total_observations-1,answer)));
    f.close();
    
def main(argv):
    
    observations = argv[1];
    answer = calculatePosteriorHypothesis(observations.strip().upper());
    writeOutputToFile(answer,observations);
    print "Finised calculating..... \nCheck output in result text file"
    
if __name__ == '__main__':
    main(sys.argv)
