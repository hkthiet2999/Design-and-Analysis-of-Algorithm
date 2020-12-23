def bubble_sort(a):
    n = len(a)
 
    for i in range(n):
 
        for j in range(0, n-1-i):
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
    print("bubble sort:")
    print(a)
 
# Driver code to test above
list = [64, 34, 25, 12, 22, 11, 90]
 
bubble_sort(list)