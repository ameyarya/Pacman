class tictactoe:

	X = 'x'
	O = 'o'
	row = -1
	col = -1
	bestVal = float("-inf")

	def isGameOn(self,game):
		for i in range(len(game)):
			for j in range(len(game[i])):
				if game[i][j] == '_':
					return True
		return False

	def evaluate(self,game):
		
		# check for rows
		for i in range(len(game)):
			for j in range(len(game[i])):
				if game[i][0] == game[i][1] and game[i][1] == game[i][2]:
					if game[i][0] == 'x':
						return 1
					elif game[i][0] == 'o':
						return -1
		# check for columns
		for i in range(len(game)):
			for j in range(len(game[i])):
				if game[0][i] == game[1][i] and game[1][i] == game[2][i]:
					if game[0][i] == 'x':
						return 1
					elif game[0][i] == 'o':
						return -1

		# check for diagonals
		if game[0][0]==game[1][1] and game[1][1]==game[2][2]:
			if game[0][0] == 'x':
				return 1
			elif game[0][0] == 'o':
				return -1

		if game[0][2]==game[1][1] and game[1][1]==game[2][0]:
			if game[0][2] == 'x':
				return 1
			elif game[0][2] == 'o':
				return -1

		# check for a draw
		return 0

	def minimax(self,game,player):

		scores = self.evaluate(game)

		if scores == 1:
			return scores

		if scores == -1:
			return scores

		if not tictactoe().isGameOn(game):
			return scores

		if player:
			v = float("-inf")
			for i in range(len(game)):
				for j in range(len(game[i])):
					if game[i][j] == '_':
						game[i][j] = self.X
						v = max(v, self.minimax(game,False))
						game[i][j] = '_'
			return v
		else:
			v = float("inf")
			for i in range(len(game)):
				for j in range(len(game[i])):
					if game[i][j] == '_':
						game[i][j] = self.O
						v = min(v, self.minimax(game,True))
						game[i][j] = '_'
			return v

	def utility(self, state):

		if not tictactoe().isGameOn(state):
			return self.evaluate(state)

		for i in range(len(state)):
			for j in range(len(state[i])):
				if state[i][j] == '_':
					state[i][j] = self.X
					moveval = tictactoe().minimax(state,False)
					state[i][j] = '_'
					if moveval > self.bestVal:
						self.bestVal = moveval
						self.row = i
						self.col = j

		print self.row,self.col

print "Given state..."
game = [['o','o','x'],
		['x','_','o'],
		['_','_','x']]
print game
print tictactoe().utility(game)

print "Blank state..."
gameblank = [['_','_','_'],
			['_','_','_'],
			['_','_','_']]
print gameblank
tictactoe().utility(gameblank)

print "Minimax value for blank state: ", tictactoe().minimax(gameblank,True)

s0 =[['_','_','_'],
	['_','_','_'],
	['_','_','_']]

s1 =[['_','_','_'],
	['_','_','_'],
	['_','_','x']]

s2 =[['o','_','_'],
	['_','_','_'],
	['_','_','x']]

s3 =[['o','_','_'],
	['x','_','_'],
	['_','_','x']]

s4 =[['o','o','_'],
	['x','_','_'],
	['_','_','x']]

s5 =[['o','o','x'],
	['x','_','_'],
	['_','_','x']]

s6 =[['o','o','x'],
	['x','_','o'],
	['_','_','x']]

print "s0 with X's turn: ",tictactoe().minimax(s0,True) 			#Output is 0, obvious for blank state
print "s1 with O's turn: ",tictactoe().minimax(s1,False)			#Output is 0
print "s2 with X's turn: ",tictactoe().minimax(s2,True)				#Output is 1
print "s3 with O's turn: ",tictactoe().minimax(s3,False)			#Output is 0
print "s4 with X's turn: ",tictactoe().minimax(s4,True)				#Output is 1
print "s5 with O's turn: ",tictactoe().minimax(s5,False)			#Output is 1
print "s6 with X's turn: ",tictactoe().minimax(s6,True)				#Output is 1

# Since the minimax value of state s1 and s3 are 0, which was O's turn,
# it can be deduced that the player O did not played optimally at both of these states.




