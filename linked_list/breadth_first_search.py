import queue



maze = []
maze.append(['#', '#', '', 'O', '#'])
maze.append(['#', '#', '', '#', '#'])
maze.append(['#', '#', '', '#', '#'])
maze.append(['#', '#', '', '#', '#'])
maze.append(['#', 'X', '', '#', '#'])



def valid_move(moves):
	for i, row in enumerate(maze):
		if 'O' in row:
			for j, pos in enumerate(row):
				if pos == 'O':
					start = (i, j)
	
	i, j = start
	
	for move in moves:
		if move == "R":
			i += 1
		elif move == "L":
			i -= 1
		elif move == "U":
			j -= 1
		elif move == "D":
			j += 1

	if 0 <= i <= len(maze[j]) and 0 <= j <= len(maze):
		if maze[j][i] != '#':
			return True
	return False


def find_path(moves):
	for i, row in enumerate(maze):
		if 'O' in row:
			for j, pos in enumerate(row):
				if pos == 'O':
					start = (i, j)
	
	i, j = start


	for move in moves:
		if move == "R":
			i += 1
		elif move == "L":
			i -= 1
		elif move == "U":
			j -= 1
		elif move == "D":
			j += 1

	if maze[i][j] == "X":
		print('found ' + moves)
		return True

	return False


moves = queue.Queue()
moves.put('')
path = ''

while not find_path(path):
	add = moves.get
	for move in ['R', 'L', 'U', 'D']:
		put = path + move
		if valid_move(move):
			moves.put(put)