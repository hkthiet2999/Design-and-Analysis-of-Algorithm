import sys

#graph
graph = {
    #start point with end point and their distance
    'a' : {'b': 3, 'c': 4, 'd': 7},
    'b' : {'c': 1, 'f': 5},
    'c' : {'f': 6, 'd': 2},
    'd' : {'e': 3, 'g': 6},
    'e' : {'g': 3, 'h': 4},
    'f' : {'e': 1, 'h': 8},
    'g' : {'h': 2},
    'h' : {'g': 2}
}

def Dijkstra(graph, start, endPoint):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    INF = sys.maxsize
    track_path = []
    
    for node in unseenNodes:
        shortest_distance[node] = INF
    shortest_distance[start] = 0
    
    while unseenNodes:
        min_distance_node = None
        
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        path_options = graph[min_distance_node].items()
        
        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node
        unseenNodes.pop(min_distance_node)
        
    currentNode = endPoint
    
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
            
        except KeyError:
            print("Path is not reachable")
            break
    track_path.insert(0, start)
    
    if shortest_distance[endPoint] != INF:
        print("Shortest Path from", start, "to", endPoint, ":")
        print("Shortest distance is " + str(shortest_distance[endPoint]))
        print("Optimal path is " + str(track_path))
        
startPoint = 'a'
endPoint = 'h'
Dijkstra(graph, startPoint, endPoint)