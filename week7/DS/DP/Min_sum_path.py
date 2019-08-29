# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

def find_min_sum_path(matrix):
	out = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
	out[0][0] = matrix[0][0]
	for i in range(1, len(matrix)):
		out[i][0] = out[i-1][0]+matrix[i][0]
	for i in range(1, len(matrix[0])):
		out[0][i] = out[0][i-1]+matrix[0][i]
	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[0])):
			out[i][j] = matrix[i][j] + min(out[i-1][j], out[i][j-1])
	return out[-1][-1]
	
matrix = [[1,3,1],[1,5,1],[4,2,1]]
print(find_min_sum_path(matrix))	