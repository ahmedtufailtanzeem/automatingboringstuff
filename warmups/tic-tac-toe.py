import sys

# Board represent's the area where game is placed. resembles #
the_board = {
	'tl': ' ', 'tm': ' ', 'tr': ' ',
	'ml': ' ', 'mm': ' ', 'mr': ' ',
	'bl': ' ', 'bm': ' ', 'br': ' '
}


def print_board(board):
	print(board['tl'] + "|" + board['tm'] + "|" + board['tr'] + "|")
	print("-+-+-")
	print(board['ml'] + "|" + board['mm'] + "|" + board['mr'] + "|")
	print("-+-+-")
	print(board['bl'] + "|" + board['bm'] + "|" + board['br'] + "|")


def game_status(the_board, turn):
		# row wise
	if (the_board['tl'] == the_board['tm'] == the_board['tr'] == turn or
		the_board['ml'] == the_board['mm'] == the_board['mr'] == turn or
		the_board['bl'] == the_board['bm'] == the_board['br'] == turn or
		# column wise
		the_board['tl'] == the_board['ml'] == the_board['bl'] == turn or
		the_board['tm'] == the_board['mm'] == the_board['bm'] == turn or
		the_board['tr'] == the_board['mr'] == the_board['br'] == turn or
		# Diagonal
		the_board['tl'] == the_board['mm'] == the_board['br'] == turn or
		the_board['bl'] == the_board['mm'] == the_board['tr'] == turn):
		return True
	else:
		return False


turn = 'X'
for i in range(9):
	print_board(the_board)
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	the_board[move] = turn
	if game_status(the_board, turn):
		print('Congratulations!!! ' + turn + ' Won...')
		print_board(the_board)
		sys.exit(1)
	else:
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'

print_board(the_board)
