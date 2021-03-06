import random

def SBM(board, depth, player=None, memo=None):
	# case of the player, switch player
	# upon entering function, or initialize
	# player to be the computer (1)
	if player is None: 
		player = 1
	elif player is 1: 
		player = 2
	elif player is 2: 
		player = 1
	else: 
		print("ERROR")

	# initialize memo!
	if memo is None: 
		# memo = {}
		memo = m

	# base case for depth=0
	if depth is 0: 
		return 0

	# initializing max as a low number
	# just in case some weird computation occurs
	max = -100

	# initializing best_locn as a random available  
	# column in case it cannot be determined below
	best_locn = random.choice(board.available_cols())

	# For each available column, drop a piece into that column
	# and get the value of that move, add it to the value of the 
	# next possible move and so on 'depth' amount of times. 
	# In the end, the path with the highest value is returned.
	for i in board.available_cols(): 

		# get the value of the move
		value = board.move_value(player, i)

		# add piece to the board
		board.add_piece(player, i)

		# get the highest value of putting another piece
		# in one of the available columns. 
		b = board.immutable()
		if b in memo: 
			other_val = memo[b]
		else: 
			other_val = SBM(board, depth-1, player, memo)
			memo[b] = other_val

		# Add the value of the current move, to the highest 
		# of the next moves. 
		value = value + other_val

		# remove the piece we put into the board
		board.rm_piece(i)

		# if the value we computed is higher than 
		# the max value we computed before
		if value > max: 
			# this value becomes the new max
			max = value
			# and the piece becomes the new best location
			best_locn = i

	return best_locn

m = {((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 2, 2, 0, 0), (0, 1, 1, 2, 2, 0, 0), (0, 1, 2, 2, 1, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 2, 2, 0, 2)): 2, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (0, 2, 0, 0, 1, 0, 0), (0, 2, 1, 2, 2, 0, 0), (0, 1, 2, 2, 1, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 2, 0, 0, 0), (1, 0, 2, 1, 0, 1, 0), (2, 1, 2, 2, 0, 1, 0)): 4, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0), (0, 0, 1, 1, 0, 0, 0), (0, 0, 1, 2, 0, 2, 0), (0, 1, 2, 2, 1, 2, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 2, 2, 0, 0), (1, 0, 0, 2, 1, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 2, 0, 0, 0, 0, 0), (1, 1, 0, 2, 2, 0, 0)): 2, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0), (1, 1, 2, 1, 0, 0, 2), (2, 1, 2, 2, 0, 1, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 2, 2, 0, 0), (0, 0, 1, 2, 1, 0, 0), (2, 1, 2, 2, 1, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (1, 2, 2, 2, 1, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0), (2, 0, 2, 0, 0, 0, 0), (1, 0, 2, 0, 0, 0, 0), (2, 1, 2, 2, 1, 1, 0)): 1, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (0, 1, 2, 2, 1, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (0, 2, 2, 2, 1, 0, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 2, 0, 0, 0, 0, 0), (1, 1, 0, 2, 2, 0, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 0, 2, 0, 0), (1, 0, 2, 1, 2, 0, 0), (2, 1, 2, 2, 1, 1, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 2, 0, 0, 0), (0, 1, 0, 2, 0, 2, 0)): 4, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0), (0, 0, 1, 2, 0, 0, 0), (2, 1, 2, 2, 1, 2, 1)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 2), (0, 0, 1, 2, 1, 0, 1), (2, 1, 2, 2, 1, 2, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 0, 2, 0, 0, 0, 0), (1, 2, 1, 2, 0, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 2), (1, 0, 2, 1, 0, 2, 1), (2, 1, 2, 2, 0, 1, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 2, 0, 0, 0, 0, 0), (1, 1, 2, 1, 0, 0, 0), (2, 1, 2, 2, 0, 1, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 2, 0, 0, 0), (0, 0, 1, 2, 0, 0, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0), (1, 0, 2, 0, 2, 0, 0), (2, 1, 2, 2, 1, 1, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 2, 0), (0, 0, 1, 2, 2, 2, 0), (1, 1, 2, 2, 1, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (2, 2, 0, 2, 1, 0, 1)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 1, 0), (2, 0, 0, 2, 0, 2, 0)): 4, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 2, 1, 2, 0, 0, 0), (2, 1, 2, 2, 1, 2, 0)): 2, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 2, 0, 0), (0, 0, 0, 2, 2, 2, 1)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (1, 1, 2, 0, 2, 0, 0), (2, 1, 2, 2, 2, 1, 0)): 1, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0), (1, 1, 2, 0, 0, 0, 0), (2, 1, 2, 2, 0, 1, 0)): 1, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 2, 0, 0), (0, 2, 0, 2, 1, 0, 0)): 2, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 0, 1, 2, 0, 1, 0), (2, 1, 2, 2, 1, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 2), (2, 0, 0, 2, 0, 1, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0), (0, 1, 1, 2, 2, 2, 0), (2, 1, 2, 2, 1, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (2, 0, 0, 0, 2, 0, 0), (2, 0, 0, 2, 1, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 2, 0), (0, 1, 0, 2, 2, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 2), (0, 2, 1, 2, 0, 0, 2), (0, 1, 2, 2, 1, 2, 1)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 2, 0), (1, 0, 2, 0, 0, 1, 0), (1, 0, 2, 0, 0, 2, 0), (2, 1, 2, 2, 0, 1, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 0, 2, 2, 1, 2, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 2, 2, 0, 0, 0), (0, 1, 1, 2, 0, 0, 1), (0, 1, 2, 2, 1, 2, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (1, 0, 0, 2, 0, 0, 0), (2, 1, 0, 2, 0, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 2, 0), (1, 0, 0, 2, 0, 2, 1)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 2, 1, 0, 0, 0), (0, 0, 1, 2, 0, 0, 0), (0, 0, 1, 2, 2, 0, 0), (0, 1, 2, 2, 1, 2, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0, 0), (1, 2, 0, 0, 0, 0, 0), (1, 2, 2, 0, 0, 0, 0), (2, 1, 2, 2, 1, 1, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (0, 0, 0, 2, 1, 0, 0), (0, 0, 1, 2, 2, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 1, 0), (0, 0, 1, 2, 0, 2, 0), (2, 1, 2, 2, 1, 2, 0)): 4, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 2, 0, 0, 0, 2, 0), (1, 2, 0, 2, 0, 1, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 2, 0), (1, 0, 0, 0, 0, 2, 0), (1, 0, 2, 0, 0, 1, 0), (2, 1, 2, 2, 2, 1, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 2), (1, 0, 0, 2, 0, 0, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (0, 0, 0, 2, 0, 1, 0), (0, 0, 1, 2, 0, 1, 0), (0, 1, 2, 2, 1, 2, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 2, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 2, 0, 2, 0, 0, 2)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (1, 2, 2, 1, 0, 0, 1), (2, 1, 2, 2, 0, 1, 2)): 1, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 2, 0, 0, 0, 0, 0), (1, 1, 0, 0, 0, 0, 0), (2, 2, 0, 2, 0, 0, 0)): 0, \
	 ((0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 2, 0, 2, 0), (0, 0, 0, 2, 1, 2, 1)): 0}