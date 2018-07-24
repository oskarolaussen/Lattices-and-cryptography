'''This is an implementation of the LLL lattice reduction algorithm. It takes as input the basis of the lattice and its dimension
and outputs LLL reduced basis that is more orthogonal. Moreover the first vector of the reduced basis solves the approximate shortest vector of the lattice -problem.'''
def gramschmidt(basis, dimension):
	orthogonal_basis=np.empty([dimension, dimension])
	orthogonal_basis[0]=basis[0]
	b=np.zeros([dimension, dimension])
	for n in range(1, dimension):
		sum=np.zeros(dimension)
		for j in range(n):
			b[n][j]=basis[n].dot(orthogonal_basis[j])/orthogonal_basis[j].dot(orthogonal_basis[j])
		for s in range(n):
			sum=b[n][s]*orthogonal_basis[s]+sum
		orthogonal_basis[n]=np.subtract(basis[n],sum)
	return orthogonal_basis, b;

def lll(basis, dimension, gramschmidt):
	w=np.empty([dimension, dimension])
	u=np.zeros([dimension, dimension])
	w,u= gramschmidt(basis, dimension)
	k=1
	while k<dimension:
		for j in range(k-1, -1, -1):
			if abs(u[k][j])>0.5:
				basis[k]=basis[k]-(np.rint(u[k,j]))*basis[j]
				w,u=gramschmidt(basis, dimension)
		if w[k].dot(w[k])>=(0.75-u[k][k-1]**2)*(w[k-1].dot(w[k-1])):
			k=k+1
		else:
			basis[[k,k-1]]=basis[[k-1,k]]
			w,u= gramschmidt(basis, dimension)
			k=max(k-1,1)
	return basis;

import numpy as np
dimension=int(input("Dimension of the lattice: "))
original_basis=np.empty([dimension, dimension])
for i in range(dimension):
	original_basis[i]=[float(x) for x in input("Input base vector of the lattice you wish to reduce: ").split()]
reduced=lll(original_basis, dimension, gramschmidt)
print(reduced)
