''' This program is an implementation of the GGH cryptosystem. 
The user inputs the dimension and basevectors of their private key and their message.
Then the program outputs the encrypted message and decrypted message, providing that the used private key is orthogonal enough.
NOTE: GGH should NOT be used to encrypt anything as it has been broken. 
This program is just an example of how the cryptosystem works.'''

import numpy as np
ERROR_VECTOR=np.array([1, -1, 1])

def input_private_key(n):
	key=np.empty([n, n])
	for i in range(n):
		key[i]=[int(x) for x in input("Input integer coordinates of a basevector in the private key separated by a space ").split()]
	return key;

	'''generate_public_key takes as input the private key and its dimension. 
	Then it multiplies the private key with 5 random unimodular matrices from the right hand side thus creating the public key and outputs it'''
def generate_public_key(n, matrix):
	k=0
	while k<5:
		A=np.random.randint(-5,5,size=(n,n))
		if np.linalg.det(A)==1:
			matrix=np.matmul(matrix,A)
			k=k+1
	return matrix;
	
	'''encyption takes as input the message, the private key and the error vector and outputs the encrypted message.'''
def encryption(m, matrix, e):
	c=np.matmul(matrix,m)+e
	return c;
	
	'''decryption uses Babai's algorithm to decrypt the encrypted message and outputs the original message (if the private key is orthogonal enough).'''
def decryption(c, pri_key, pub_key):
	u = np.matmul(np.linalg.inv(pri_key), c)
	u=np.matmul(pri_key, np.rint(u))
	result=np.matmul(np.linalg.inv(pub_key),u)
	return result;

dimension=int(input("Input the dimension of the private key: "))
private_key=input_private_key(dimension)
public_key=generate_public_key(dimension, private_key)
message=np.empty(dimension)
message=[int(x) for x in input("Input the integer vector you wish to encrypt ").split()]
encrypted=encryption(message, public_key, ERROR_VECTOR)
print(encrypted)
decrypted=decryption(encrypted, private_key, public_key)
print(decrypted)