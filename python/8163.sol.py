def make_adjacency_matrix(edge_list):
	adjacency_matrix = []
	num = 0
	pass
	for lists in edge_list:
		for item in lists:
			if ord(item) > num:
				if (ord(item)-64) > num:
					num = ord(item)-64

	for lists in edge_list:
		adjacency = []
		i = 1
		for i in range(num):
			letter = chr(ord("A") + i)
			if letter in lists:
				adjacency.append(1)
			else:
			    adjacency.append(0)
		adjacency_matrix.append(adjacency)    
	return adjacency_matrix
