'''This program is an implementation of Babai's algorithm. The algorithm finds the closest lattice point for a given vector
providing that the used basis for the lattice is orthogonal enough.'''

import numpy as np
dimension = int(input("Dimension of lattice: " ))
basis = np.empty([dimension,dimension])
vector = np.empty([dimension])
for i in range(dimension):
	basis[i]=[float(x) for x in input("Coordinates of a base vector separated by space: ").split()]
basis = np.matrix(basis)
vector=[float(x) for x in input("Input the  vector you wish to find the closest lattice point for ").split()]
u = np.rint(np.matmul(vector, np.linalg.inv(basis)))
u=np.matmul(u,basis)
print(u)
