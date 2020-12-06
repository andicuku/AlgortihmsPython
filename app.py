game = [[1, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]


class InvalidTicTacToeGame(Exception):
	pass


def check_row(row):
	if len(row) != 3:
		raise InvalidTicTacToeGame("Invalid TicTacToe row")
	if row.count(1) == 3:
		return 1
	return 2 if row.count(2) == 3 else 0


def wining_board(board):
	for row in board:
		yield row
	for column in range(3):
		yield [row[column] for row in board]
	yield [board[i][i] for i in range(3)]

	yield [board[r][c] for (r, c) in zip(range(3), range(2, -1, -1))]


def check_winer(board):
	for line in wining_board(board):
		winner = check_winer(line)
		if winner != 0:
			return winner
		return 0


for i, line in enumerate(wining_board(game), 1):
	print(i, line, check_row(line))
check_winer(game)


