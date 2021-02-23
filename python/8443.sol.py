import numpy as np

def sol():
	l = np.array([
				[0.93, 0.73, ],
				[0.81, 0.87, ],
				[0.68, 0.5, ],
				])
	sig = 1 / (1 + np.exp(-l))
	return sig