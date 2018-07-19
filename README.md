# Lattices and cryptography

ggh.py is an implementation of the GGH cryptosystem.  The user inputs the dimension and basevectors of their private key and their message. Then the program outputs the encrypted message and decrypted message, providing that the used private key is orthogonal enough. NOTE: GGH should NOT be used to encrypt anything as it has been broken. 
This program is just an example of how the cryptosystem works.

gramschmidt.py takes as input the base vectors of a vector space and outputs an orthogonal basis for that space using the Gram-Schmidt process.

babai.py is an implementation of Babai's algorithm. The algorithm finds the closest lattice point for a given vector
providing that the used basis for the lattice is orthogonal enough.

gauss.py implements the Gauss lattice reduction algorithm. It takes as input base vectors of an 2 dimensional lattice and outputs an basis that is more orthogonal. The first vector of the output basis is the shortest non-zero vector of the lattice.


