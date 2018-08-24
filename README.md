# Lattices and cryptography

ggh.py is an is an implementation of the GGH cryptosystem. 
The user inputs the name of the file containing private key on the command line. For example
"python ggh.py input.txt". The input file must contain a square matrix with base vectors of the private key as rows.
Coordinates must be separated by a space. Then the program prompts the user for the integer vector they wish to encrypt.
Then the program outputs the encrypted message and decrypted message, providing that the used private key is orthogonal enough.
NOTE: GGH should NOT be used to encrypt anything as it has been broken. 
This program is just an example of how the cryptosystem works.

lll.py is an implementation of the LLL lattice reduction algorithm. It takes as input the basis of the lattice and its dimension
and outputs LLL reduced basis that is more orthogonal. Moreover the first vector of the reduced basis solves the approximate shortest vector problem.

gramschmidt.py takes as input the base vectors of a vector space and outputs an orthogonal basis for that space using the Gram-Schmidt process.

babai.py is an implementation of Babai's algorithm. The algorithm finds the closest lattice point for a given vector
providing that the used basis for the lattice is orthogonal enough.

gauss.py implements the Gauss lattice reduction algorithm. It takes as input base vectors of an 2 dimensional lattice and outputs an basis that is more orthogonal. The first vector of the output basis is the shortest non-zero vector of the lattice.


