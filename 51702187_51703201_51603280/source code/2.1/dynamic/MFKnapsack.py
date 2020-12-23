import time
import pylab
def MF_knapsack(i, wt, val, j):
    global F  # a global dp table for knapsack
    if F[i][j] < 0:
        if j < wt[i - 1]:
            val = MF_knapsack(i - 1, wt, val, j)
        else:
            val = max(
                MF_knapsack(i - 1, wt, val, j),
                MF_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
            )
        F[i][j] = val
    return F[i][j]

# len(val) = len(wt) = 3
val = [60, 100, 120]
wt = [10, 20, 30]
w = 50
# len(val) = len(wt) = 10
val_1 = [800, 1200, 1400, 1800, 2200, 2400, 2600, 3000, 4000, 5000]
wt_1 = [600, 1200 , 2400, 3600, 4800, 5000, 5200, 6000, 8000, 9000]
w_1 = 50000
# len(val) = len(wt) = 50
val_2 = [1, 2, 7, 9, 4, 6, 23, 4, 5, 7, 1, 22, 65, 91, 34, 26, 23, 11, 55, 97, 64, 2, 2, 9,12, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10, 12, 14, 16, 1, 2, 3, 5, 7, 5, 9, 6, 29, 92, 99, 21]
wt_2 = [5, 10, 15, 20, 25, 30, 25, 20, 15, 10, 12, 14, 16, 1, 2, 3, 5, 7, 5, 9, 6, 29, 92, 99, 21, 1, 2, 7, 9, 4, 6, 23, 4, 5, 7, 1, 22, 65, 91, 34, 26, 23, 11, 55, 97, 64, 2, 2, 9,12]
w_2 = 300
# --------------------
n = len(val)
F = [[0] * (w + 1)] + [[0] + [-1 for i in range(w + 1)] for j in range(n + 1)]
# main
start = time.time()
result_0 = MF_knapsack(n, wt, val, w)
print(result_0)
time_0 = time.time() - start
print(time_0)
# --------------------
n = len(val_1)
F = [[0] * (w_1 + 1)] + [[0] + [-1 for i in range(w_1 + 1)] for j in range(n + 1)]
# main
start = time.time()
result_1 = MF_knapsack(n, wt_1, val_1, w_1)
print(result_1)
time_1 = time.time() - start
print(time_1)
# --------------------
n = len(val_2)
F = [[0] * (w_2 + 1)] + [[0] + [-1 for i in range(w_2 + 1)] for j in range(n + 1)]
# main
start = time.time()
result_2 = MF_knapsack(n, wt_2, val_2, w_2)
print(result_2)
time_2 = time.time() - start
print(time_2)
#-------------------------
pylab.plot([time_0,time_1,time_2],[3,10,50], 'o-')
pylab.show()