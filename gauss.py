#This program implements the Gauss lattice reduction algorithm. It takes as input base vectors of an 2 dimensional lattice and outputs an basis that is more orthogonal.
#The first vector of the output basis is the shortest non-zero vector of the lattice.


import numpy as np
a, b = input("Coordinates of first base vector: ").split()
c, d = input("Coordinates of second base vector: ").split()
v = np.array([float(a), float(b)])
w=np.array([float(c), float(d)])
m=1
while m!=0:
	if np.linalg.norm(v)>np.linalg.norm(w):
		v, w= w, v	
	m=np.rint((np.dot(v,w))/np.linalg.norm(v)**2)
	if m==0:
		print("New basis is ", v, " and ", w ,".")
	else:
		w=w-m*v