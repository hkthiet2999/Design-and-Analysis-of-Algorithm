import math

def Prim(G,V):
	Vt = [] 
	Vt.append(V[0])
	Et = []
	#print(len(V)-1)
	for i in range(len(V)-1):
		#print(i)
		min = math.inf
		for v in Vt:
			Vs = [e for e in V if e not in Vt]
			#print(Vs)
			for u in Vs:
				if(G[V.index(v)][V.index(u)]==0):
					continue
				if(G[V.index(v)][V.index(u)]<min):
					min = G[V.index(v)][V.index(u)]
					vmin, umin = v, u
					#print(vmin,umin)
		Vt.append(umin)
		Et.append([vmin,umin])
	return Et
	
def main():
	G = [[0, 6, 3, 0, 7, 0],
	[6, 0, 4, 2, 0, 5],
	[3, 4, 0, 3, 8, 0],
	[0, 2, 3, 0, 0, 2],
	[7, 0, 8, 0, 0, 0],
	[0, 5, 0, 2, 0, 0]]
	V = ['A','B','C','D','E','F']
	print(Prim(G,V))
main()