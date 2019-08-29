def unique_paths(m, n):
	path_count = [[0 for i in range(n)] for j in range(m)]
	for i in range(m):
		path_count[i][0] = 1
	for i in range(n):
		path_count[0][i] = 1
	for i in range(1, m):
		for j in range(1, n):
			path_count[i][j] = path_count[i-1][j] + path_count[i][j-1]
	return path_count[-1][-1]		

print(unique_paths(3, 5))			