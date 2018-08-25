# Lattices and cryptography

ggh.py is an is an implementation of the GGH cryptosystem. 
The user inputs the name of the file containing private key on the command line. For example
"python ggh.py input.txt". The input file must contain a square matrix with base vectors of the private key as rows.
Coordinates must be separated by a space. Then the program prompts the user for the integer vector they wish to encrypt.
Then the program outputs the encrypted message and decrypted message, providing that the used private key is orthogonal enough.
NOTE: GGH should NOT be used to encrypt anything as it has been broken. 
This program is just an example of how the cryptosystem works.

lll.py This is an implementation of the LLL lattice reduction algorithm. The user inputs the name of the file containing the basis on the command line. For example
"python lll.py input.txt". The input file must contain a square matrix with base vectors of the lattice as rows.
Coordinates must be separated by a space.
The program then outputs LLL reduced basis that is more orthogonal. Moreover the first vector of the reduced basis solves the approximate shortest vector problem.

gramschmidt.py takes as input the base vectors of a vector space and outputs an orthogonal basis for that space using the Gram-Schmidt process.
The user inputs the name of the file containing the basis on the command line. For example
"python gramschmidt.py input.txt". The input file must contain the base vectors of as lines.
Coordinates must be separated by a space.

gauss.py implements the Gauss lattice reduction algorithm. It takes as input 
base vectors of an 2 dimensional lattice and outputs an basis that is more orthogonal.
The user inputs the name of the file containing the basis on the command line. For example
"python gauss.py input.txt". The input file must contain a square matrix with base vectors of the lattice as rows.
Coordinates must be separated by a space.
The first vector of the output basis is the shortest non-zero vector of the lattice.
