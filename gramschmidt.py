#This program takes as input the base vectors of a vector space and outputs an orthogonal basis for that space using the Gram-Schmidt process.

import numpy as np
number_of_vectors=int(input("Number of base vectors: "))
dimension=int(input("Dimension of vectors: "))
basis=np.empty([number_of_vectors, dimension])
for i in range(number_of_vectors):
	basis[i]=[float(x) for x in input("Coordinates of a base vector separated by space: ").split()]
orthogonal_basis=np.empty([number_of_vectors, dimension])
orthogonal_basis[0]=basis[0]
u=np.zeros([number_of_vectors, dimension])
for n in range(1, number_of_vectors):
	sum=np.zeros(dimension)
	for j in range(n):
		u[n][j]=basis[n].dot(orthogonal_basis[j])/orthogonal_basis[j].dot(orthogonal_basis[j])
	for k in range(n):
		sum=u[n][k]*orthogonal_basis[k]+sum
	orthogonal_basis[n]=np.subtract(basis[n],sum)
print(orthogonal_basis)