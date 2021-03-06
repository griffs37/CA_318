import numpy as np

def sol():
	X = np.array( ([3,5],[5,1],[10,2]) , dtype = float)
	y = np.array( ([75], [82], [93]) , dtype = float)
	X = X / np.amax(X,axis=0)
	y = y / 100
	size_input = np.shape(X)[1] # number of columns of X
	size_hidden = 3
	size_output = 1
	np.random.seed(145)
	W1 = np.random.randn(size_input, size_hidden)
	return np.dot(X, W1)