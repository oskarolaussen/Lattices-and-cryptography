'''This is an implementation of the LLL lattice reduction algorithm. The user inputs the name of the file containing the basis on the command line. For example
"python lll.py input.txt". The input file must contain a square matrix with base vectors of the lattice as rows.
Coordinates must be separated by a space.
The program then outputs LLL reduced basis that is more orthogonal. Moreover the first vector of the reduced basis solves the approximate shortest vector of the lattice -problem.'''

import numpy as np
import sys

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
	return orthogonal_basis, b

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
	return basis

def input_handler(filename):
	try:
		with open(filename, 'r') as infile:
			n = sum((1 for line in infile))
			matrix = np.empty([n, n])
			i = 0
			infile.seek(0)
			for line in infile:
				matrix[i] = [int(x) for x in line.split()]
				i = i + 1
	except Exception as e:
		print(e)
	return matrix, n
	
filename = sys.argv[-1]
original_basis, dimension = input_handler(filename)
reduced=lll(original_basis, dimension, gramschmidt)
print(reduced)
