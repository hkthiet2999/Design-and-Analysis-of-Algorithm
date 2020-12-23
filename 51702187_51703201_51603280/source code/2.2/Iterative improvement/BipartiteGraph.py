import numpy as np
import time
import pylab
class GFG: 
    def __init__(self,graph): 
        self.graph = graph  
        self.ppl = len(graph) 
        self.jobs = len(graph[0]) 
  
    def bpm(self, u, matchR, s): 
        for v in range(self.jobs): 
            if self.graph[u][v] and s[v] == False:    
                s[v] = True 
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, s): 
                    matchR[v] = u 
                    return True
        return False

    def maxBPM(self): 
        matchR = [-1] * self.jobs 
        result = 0
        for i in range(self.ppl):               
            s = [False] * self.jobs              
            if self.bpm(i, matchR, s): 
                result += 1
        return result 
  
gr2 =[[0, 1, 1, 0, 0, 0], 
          [1, 0, 0, 1, 0, 0], 
          [0, 0, 1, 0, 0, 0], 
          [0, 0, 1, 1, 0, 0], 
          [0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 1]] 
gr3 =[[0, 1, 1, 0, 0, 0], 
          [1, 0, 0, 1, 0, 0], 
          [0, 0, 0, 0, 0, 0], 
          [0, 0, 1, 0, 0, 1], 
          [0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 1]]  
gr1 =[[0, 1, 1, 0, 0, 0], 
          [1, 0, 0, 1, 0, 0], 
          [0, 0, 1, 0, 1, 0], 
          [0, 0, 1, 1, 0, 1], 
          [0, 0, 0, 0, 0, 0]] 
gr4 =[[0, 1, 1, 0, 0, 0, 0], 
          [1, 0, 0, 1, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 1], 
          [0, 0, 1, 0, 0, 1, 1], 
          [0, 0, 0, 0, 0, 0, 1], 
          [0, 0, 0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 1]]

start = time.time()  
g1 = GFG(gr1) 
print ("Maximum Matching in Bipartite Graphs: %d " % g1.maxBPM()) 
time_1 = time.time() - start
print(time_1)

#start = time.time()  
g2 = GFG(gr2) 
print ("Maximum Matching in Bipartite Graphs: %d " % g2.maxBPM()) 
time_2 = time.time() - start
print(time_2)

#start = time.time()  
g3 = GFG(gr3) 
print ("Maximum Matching in Bipartite Graphs: %d " % g3.maxBPM()) 
time_3 = time.time() - start
print(time_3)

#start = time.time()  
g4 = GFG(gr4) 
print ("Maximum Matching in Bipartite Graphs: %d " % g4.maxBPM()) 
time_4 = time.time() - start
print(time_4)

#-------------------------
pylab.plot([time_1,time_2,time_3, time_4],[4,6,7,8], 'o-')
pylab.show()

