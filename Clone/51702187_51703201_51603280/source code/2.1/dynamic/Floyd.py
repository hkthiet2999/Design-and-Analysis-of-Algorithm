import time
import pylab
def floyd(G, nV):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance, nV)

def print_solution(distance, nV):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == 99999:
                print('INF', end="  ")
            else:
                print(distance[i][j], end="  ")
        print(" ")
INF = 99999
# # Input 1:
nV_1 = 4
G_1 = [[0, 7, INF, 9],
    [1, 0, INF, 6],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]]
# Input 2:
nV_2 = 6
G_2 = [[0, 1, INF, INF, 10, INF ],
    [INF, 0, INF, INF, 9, INF],
    [INF, 1, 0, INF, 10, 1],
    [INF, INF, INF, 0, INF, 1],
    [INF, 3, 2, INF, 0, 3],
    [INF, 4, 3, 6, INF, 0]]
# Input 3:
nV_3 = 9
G_3 = [[0, 4, INF, INF, INF, INF, INF, 8, INF], 
    [4, 0, 8, INF, INF, INF, INF, 11, INF], 
    [INF, 8, 0, 7, INF, 4, INF, INF, 2], 
    [INF, INF, 7, 0, 9, 14, INF, INF, INF], 
    [INF, INF, INF, 9, 0, 10, INF, INF, INF], 
    [INF, INF, 4, 14, 10, 0, 2, INF, INF], 
    [INF, INF, INF, INF, INF, 2, 0, 1, 6], 
    [8, 11, INF, INF, INF, INF, 1, 0, 7], 
    [INF, INF, 2, INF, INF, INF, 6, 7, 0]]
start = time.time()
print('Floyd Algorithm - Input 1: ')
floyd(G_1, nV_1)
time_1 = time.time() - start
print(time_1)

start = time.time()
print('Floyd Algorithm - Input 2: ')
floyd(G_2, nV_2)
time_2 = time.time() - start
print(time_2)
start = time.time()
print('Floyd Algorithm - Input 3: ')
floyd(G_3, nV_3)
time_3 = time.time() - start
print(time_3)
#-------------------------
pylab.plot([time_1,time_2,time_3],[4,6,9], 'o-')
pylab.show()