"""
print the board below
"""
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def print_board(bo):
	count = 0
	for i in bo:

		print("| ", end="")
		for j in range(len(i)):
			print(i[j], end=" ")
			if (j+1)%3==0:
				print(" | ", end="")
		count += 1
		print()
		if count%3==0:
			print("-- -- -- -- -- -- -- -- --")

def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[i])):
			if bo[i][j]==0:
				return (i,j)
	return None

def valid(bo, pos, num):
	"""
	Returns if the attempted move (inserted 'num') is valid
	param bo: 2d list of ints
	param pos: (row, col)
	param num: int
	return: bool
	"""

	# check along the rows
	for i in range(len(bo)):
		if bo[pos][]:
			pass

print_board(board)
find_empty(board)