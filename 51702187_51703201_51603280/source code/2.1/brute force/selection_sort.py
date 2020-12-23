def selection_sort(a):
	for i in range(len(a)-1):
		m = i
		for j in range(i+1, len(a)): 
			if(a[j]<a[m]):
				m = j
		a[i],a[m]=a[m],a[i]
	print("selection sort:")
	print(a)

list = [23,5,30,25,1,6,8,35]
selection_sort(list)