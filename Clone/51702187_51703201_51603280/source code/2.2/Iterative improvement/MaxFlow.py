import numpy as np
import time
import pylab
class Graph ():
    '''
    A flow graph object
    Calculates max flow using different methods
    '''

    def __init__(self, data=None):
        n, m = np.shape(data)
        assert n == m, "data must be square"

        # edge properties
        self.capacity = data
        self.flow = np.zeros((n, n), dtype=np.int)

        self.size = n

        # vertices properties
        self.vertices = np.array([i for i in range(self.size)])
        self.excess = [0] * self.size
        self.distance = [0] * self.size
        self.level = [-1] * self.size
        self.seen = [0] * self.size


        assert sum(self.capacity[-1]) == 0 and sum(self.capacity[:, 0]) \
        == 0 , "source must be first, sink must be last"

        self.source = 0
        self.sink = self.size - 1

    def _search(self, traverse, origin=None, goal=None, DFS=False):
        '''
        objective : find an augmented path between given origin and goal.
        uses DFS or BFS
        parameters :
            self - object
            traverse - a 1D array, holds the traverse of the path,
                traverse[successor] = current
            origin - int, an index for the origin, the default is the source
            goal - int, an index for the goal, the default is sink
            DFS - bool, True will search depth-first and False will
                search breadth-first.
            the default is BFS
        output
            True or False; indicator whether a path exists
        '''

        # set path origin and goal indexes
        goal = goal or self.sink
        origin = origin or self.source

        # avoid double visit
        visited = [False] * self.size

        # a queue that states the next indexes to visit, starting with origin
        to_visit = [origin]

        # mark origin as visited
        visited[origin] = True

        # to determine the edge; predecessor:u 
        predecessor = origin

        while to_visit:

            # pops the next index to visit, base of the search method chosen
            if DFS:
                current = to_visit.pop(0)
            # BFS
            else:  
                current = to_visit.pop()

            # iterates on all possible steps
            for successor in range(self.size):

                # a viable next step is one that was not visited and that its 
                # residual is possitive
                if (not visited[successor]) and \
                (self.capacity[(current, successor)] \
                    - self.flow[(current, successor)] > 0):

                    # mark as visited and add to the queue to explore
                    visited[successor] = True
                    to_visit.append(successor)

                    # adds to the traverse
                    traverse[successor] = current

        return visited[goal]

    def _max_flow_search_FF(self, origin=None, goal=None, data=False,\
     DFS=False):
        '''
        objective : finds the max flow for a given graph
        parameters :
            self - object
            origin - int, an index for the origin, the default is the source
            goal - int, an index for the goal, the default is sink
            data - bool, returns extended information if marked True
            DFS - bool, True will search depth-first and False will search 
            breadth-first. the default is BFS
        output
            default - float of max flow
            with data - {max_flow: float of max flow, iteration: 
             a dictionary with all traverses taken}
    
        complexity 
            O(VE^2)
        '''

        goal = goal or self.sink
        origin = origin or self.source

        #extendend information 
        presented_data = {}

        # initiate vars
        traverse = [-1] * self.size
        max_flow = 0
        iter_count = 0
        path_flow = float('inf')

        # before augmented path were exhusted 
        while self._search(traverse, origin, goal, DFS):

            iter_count += 1
            presented_data[iter_count] = []

            # walk backwards, find the smallest viable flow 
            # for an augmented path
            current = goal
            while current != origin :

                presented_data[iter_count].append(current)

                # the predecessor for the current index 
                pred = traverse[current]

                # calculate the residual, the path flow is the smaller 
                # between the edge residual and the existinf flow
                residual_flow = (self.capacity[(pred, current)] - \
                    self.flow[(pred, current)])
                path_flow = min(path_flow, residual_flow)

                current = pred

            # add the current path flow to the total flow
            max_flow += path_flow

            # walk backwards, update the flow on the edges based on 
            # the path flow
            current = goal
            while current != origin :

                # the predecessor for the current index 
                pred = traverse[current]

                self.flow[(pred, current)] += path_flow
                self.flow[(current, pred)] -= path_flow

                current = pred

        if data:
            return {'max_flow' : max_flow, 'iteration': \
            [{i: [0] + presented_data[i][::-1]} \
            for i  in range(1, iter_count+1)]}
        return max_flow

    def EdmondKarp(self, origin=None, goal=None, data=False):
        '''
        objective : an external func, uses _max_flow_search with BFS 
            Finds the shortest augmenting path from s to t, using BFS.
            For each path, it finds the bounding capacity and sends as 
            much flow. This process is repeating until there are no more 
            augmented path in the residual graph
        parameters :
            self - object
            origin - int, an index for the origin, the default is the source
            goal - int, an index for the goal, the default is sink
            data - bool, returns extended information if marked True
            
        output
            default - float of max flow
            with data - {max_flow: float of max flow, iteration: a dictionary 
                with all traverses taken}
        
        complexity 
            O(VE^2)
            This algorithm uses a BFS to fins in each iteration the shortest 
            augmented path between the source and the sink. Each path contains 
            at least one edge. A single BFS runs O(E) and a push along the 
            path is in its worst case O(E). Since the length of th paths 
            never decreases (as promised by the use of BFS) and the length 
            of a path can never exceed V, each edge can be found V times.
            The total complexity, therefore, O(VE^2)
            
        '''
        return self._max_flow_search_FF(origin=origin, goal=goal, \
            data=data, DFS=False)
# Input 3:
G_3 = np.array([[0, 10, 0, 8, 0, 0, 0],
                [0, 0, 5, 0, 2, 0, 0],
                [0, 0, 0, 4, 6, 0, 0],
                [0, 0, 0, 0, 10, 5, 0],
                [0, 7, 0, 0, 0, 10, 0],
                [0, 0, 0, 2, 0, 5, 0],
                [0, 0, 0, 0, 0, 0, 0]])
#------------
# Input 2:
G_2 = np.array([[0, 10, 0, 8, 0, 0],
                [0, 0, 5, 2, 0, 0],
                [0, 0, 0, 0, 0, 7],
                [0, 0, 0, 0, 10, 0],
                [0, 0, 8, 0, 0, 10],
                [0, 0, 0, 0, 0, 0]])
#Input 1:
G_1 = np.array([[0, 7, 0, 9],
                [0, 0, 0, 6],
                [0, 1, 0, 0],
                [0, 0, 0, 0]])
start = time.time()
EdmondKarp_graph = Graph(G_1)
print("Max flow using shortest-augmenting-path - Input 4x4 :")
print(EdmondKarp_graph.EdmondKarp())
time_1 = time.time() - start
print(time_1)
#---
# start = time.time()
EdmondKarp_graph = Graph(G_2)
print("Max flow using shortest-augmenting-path - Input 6x6 :")
print(EdmondKarp_graph.EdmondKarp())
time_2 = time.time() - start
print(time_2)
#---
# start = time.time()
EdmondKarp_graph = Graph(G_3)
print("Max flow using shortest-augmenting-path - Input 7x7 :")
print(EdmondKarp_graph.EdmondKarp())
time_3 = time.time() - start
print(time_3)
#-------------------------
pylab.plot([time_1,time_2,time_3],[4,6,7], 'o-')
pylab.show()

