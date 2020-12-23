import time
import pylab
INT_MAX = 2147483647

def optimalSearchTree(keys, P, n): 

    C = [[0 for x in range(n)]  
               for y in range(n)] 

    for i in range(n): 
        C[i][i] = P[i]  

    for d in range(2, n + 1): 
        for i in range(n - d + 2): 

            j = i + d - 1
            if i >= n or j >= n: 
                break
            C[i][j] = INT_MAX 

            for k in range(i, j + 1): 

                c = 0
                if (k > i): 
                    c += C[i][k - 1] 
                if (k < j): 
                    c += C[k + 1][j] 
                sum = 0
                for s in range(i, j + 1): 
                    sum += P[s]  
                c += sum  
                if (c < C[i][j]): 
                    C[i][j] = c 
    return C[0][n - 1]  
  
# Driver Code 
if __name__ == '__main__': 
    # n = len(keys_1) = len(freq_1) = 3
    keys_0 = [10, 12, 20] 
    freq_0 = [34, 8, 50] 
    # n = len(keys_1) = len(freq_1) = 10
    keys_1 = [800, 1200, 1400, 1800, 2200, 2400, 2600, 3000, 4000, 5000]
    freq_1 = [600, 1200 , 2400, 3600, 4800, 5000, 5200, 6000, 8000, 9000]
    # n = len(keys_1) = len(freq_1) = 50
    keys_2 = [1, 2, 7, 9, 4, 6, 23, 4, 5, 7, 1, 22, 65, 91, 34, 26, 23, 11, 55, 97, 64, 2, 2, 9,12, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10, 12, 14, 16, 1, 2, 3, 5, 7, 5, 9, 6, 29, 92, 99, 21]
    freq_2 = [5, 10, 15, 20, 25, 30, 25, 20, 15, 10, 12, 14, 16, 1, 2, 3, 5, 7, 5, 9, 6, 29, 92, 99, 21, 1, 2, 7, 9, 4, 6, 23, 4, 5, 7, 1, 22, 65, 91, 34, 26, 23, 11, 55, 97, 64, 2, 2, 9,12]

    #-----------------------
    n = len(keys_0) 
    start = time.time()
    print("Cost of Optimal BST is", optimalSearchTree(keys_0, freq_0, n)) 
    time_0 = time.time() - start
    print(time_0)
    #-----------------
    start = time.time()
    print("Cost of Optimal BST is", optimalSearchTree(keys_1, freq_1, n)) 
    time_1 = time.time() - start
    print(time_1)
    #-----------------
    start = time.time()
    print("Cost of Optimal BST is", optimalSearchTree(keys_2, freq_2, n)) 
    time_2 = time.time() - start
    print(time_2)
    #-----------------
    pylab.plot([time_0,time_1,time_2],[3,10,50], 'o-')
    pylab.show()
   
