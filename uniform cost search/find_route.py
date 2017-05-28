import heapq
import sys;

explored = []
graph = {}
tracedNodes = {};

class GetInputData:

        def readInputFile(self,filename):
         
                file = open(filename);
                lines = file.readlines();

                for line in lines:
                   
                    rowWiseData = line.split();

                    if rowWiseData[0] == "END" and rowWiseData[1] == "OF":
                        
                        break;
                    elif rowWiseData[0] in graph:

                        graph[rowWiseData[0]][rowWiseData[1]] = rowWiseData[2];
                        if rowWiseData[1] in graph:
                            graph[rowWiseData[1]][rowWiseData[0]] = rowWiseData[2];
                        else:
                            graph[rowWiseData[1]] = {};
                            graph[rowWiseData[1]][rowWiseData[0]] = rowWiseData[2];
                    else:
                        graph[rowWiseData[0]] = {};
                        graph[rowWiseData[0]][rowWiseData[1]] = rowWiseData[2];
                        if rowWiseData[1] in graph:
                            graph[rowWiseData[1]][rowWiseData[0]] = rowWiseData[2];
                        else:
                            graph[rowWiseData[1]] = {};
                            graph[rowWiseData[1]][rowWiseData[0]] = rowWiseData[2];

class PriorityQueue:

	def __init__(self):
		self._queue = []

	def addElement(self, item, priority): #insert the item in the queue and assign the priority
		heapq.heappush(self._queue, (priority, item))

	def deleteElement(self):
		return heapq.heappop(self._queue)[-1]

	def isEmpty(self):
		return len(self._queue) == 0

class Ucs:
        #This function finds the optimal path from source to destination using UCS algorithm
        def tracePath(self,graph, start, dest,queue):

                while True:
                        
                        if queue.isEmpty(): #checks whether there is reachable path between the given source and destination 
                                
                                print "distance:infinity";
                                print "route:";
                                print "none";
                                break;
                        
                        nodeTemp, cost = queue.deleteElement() #Remove the node having the least cost
                        nodePathTemp = nodeTemp.split(':');
                        node = nodePathTemp[-1];
                        if self.testGoal(dest, node): #tests for the goal state
                                
                                print "distance: ",str(cost)+" km";
                                print "route:";
                                i = 0;
                                while(i<len(nodePathTemp)-1):
                                        print nodePathTemp[i]+" to "+nodePathTemp[i+1]+", "+graph[nodePathTemp[i]][nodePathTemp[i+1]]+" km";
                                        i= i+1;
                                break;
                        else:
                                for child in self.getChildNodes(node, graph):
                                        
                                        if child in explored:
                                                pass
                                        else:
                                                explored.append(node)
                                                pathCost = cost + int(graph[child][node]) #finds the cost from the current node to each child from source
                                                nodePath = nodeTemp+":"+child;
                                                queue.addElement((nodePath,pathCost),pathCost);

        def getChildNodes(self,node, graph):

                childrens = graph[node]
                if len(childrens) == 0:
                       print "No node ahead";
                return childrens

        def testGoal(self,dest, node):
                if dest == node:
                        return True
                else:
                        return False

if __name__ == "__main__":

    getInput = GetInputData();
    filename = sys.argv[1];
    getInput.readInputFile(filename);
    source= sys.argv[2];
    destination = sys.argv[3];
    queue = PriorityQueue()
    queue.addElement((source, 0), 0)
    ucs = Ucs();
    ucs.tracePath(graph, source, destination,queue);
