def make_edge_list(adjacency):

	edge_list = []
	for lists in adjacency:
		edge =[]
		i = 0
		for item in lists:
			if item ==1:
				letter = chr(ord("A") + i)
				edge.append(letter)
			i += 1
		edge_list.append(edge)


	return edge_list