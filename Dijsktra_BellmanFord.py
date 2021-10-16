import sys

class Graph():

#-----------Dijkstra-----------

    #Αρχικοποίηση κόμβων
    def __init__(self, vertices):
    	self.V = vertices
    	self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    	
    #Εκτύπωση Αποτελέσματος
    def printSolution(self, dist):
    	print("Πίνακας δρομολόγησης για κόμβο-αφαιτηρία " + str(sNode))
    	for node in range(self.V):
    		print("Kόστος μέχρι τον κόμβο " + str((node+1)) + ": ", dist[node])

    #Εύρεση κόμβου ελάχιστης διαδρομής
    def minDistance(self, dist, tree):

    	min = sys.maxsize

    	for v in range(self.V):
    		if dist[v] < min and tree[v] == False:
    			min = dist[v]
    			min_index = v

    	return min_index

    #Υλοποίηση αλγορίθμου Dijkstra
    def dijkstra(self, src):

    	dist = [sys.maxsize] * self.V
    	dist[src] = 0
    	tree = [False] * self.V

    	for cout in range(self.V):
            
    		u = self.minDistance(dist, tree)

    		tree[u] = True

    		for v in range(self.V):
    			if self.graph[u][v] > 0 and tree[v] == False and dist[v] > dist[u] + self.graph[u][v]: dist[v] = dist[u] + self.graph[u][v]

    	self.printSolution(dist)
    	
#-----------Belmand-Ford-----------

    #Αρχικοποίηση πλήθους κόμβων
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []
 
    #Εισαγωγή νέου μονοπατιού στο γράφο
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
         
    #Εκτύπωση Αποτελέσματος
    def printArr(self, dist):
        print("Πίνακας δρομολόγησης για κόμβο-αφαιτηρία " + str(sNode))
        print("{0}\t\t{1}".format("Κόμβος", "Κόστος από κόμβο-αφαιτηρία"))
        for i in range(self.V):
            print("{0}\t\t{1}".format(i+1, dist[i]))
     
    #Υλοποίηση αλγορίθμου Bellman Ford
    def BellmanFord(self, src):
 
        dist = [float("Inf")] * self.V
        dist[src] = 0
 
        for _ in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        self.printArr(dist)
    	
    #Επιλογή αλγορίθμου	
    def shortestPath(self, alg, sNode):
        if alg == "d":
        #Αρχικοποίηση γράφου
            g.graph = [     [0, 6, 0, 12, 0, 0],
                            [6, 0, 5, 2, 3, 0],
                            [0, 5, 0, 0, 3, 10],
                            [12, 2, 0, 0, 5, 0],
                            [0, 3, 3, 5, 0, 1],
                            [0, 0, 10, 0, 1, 0]
                            ]
            g.dijkstra(sNode - 1)
        else:
            g.addEdge(0, 1, 6)
            g.addEdge(0, 3, 12)
            g.addEdge(1, 2, 5)
            g.addEdge(1, 3, 2)
            g.addEdge(1, 4, 3)
            g.addEdge(2, 4, 3)
            g.addEdge(2, 5, 10)
            g.addEdge(3, 4, 5)
            g.addEdge(4, 5, 1)
            
            g.BellmanFord(sNode - 1)


#----Κυρίως πρόγραμμα----
g = Graph(6)

print("Επιλέξτε αλγόριθμου υπολογισμού ελάχιστης διαδρομής: (d για Dijkstra και b για Bellman-Ford)")
algorithm = input()

print("Επιλέξτε κόμβο αφαιτηρίας: (1 εώς 6)")
sNode = int(input())
g.shortestPath(algorithm, sNode)                    


input('Press ENTER to exit')

