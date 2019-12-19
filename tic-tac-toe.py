class tictactoe:

	turn = 'x'
	player = 'x'
	opponent = 'o'
	bestValue = -1000
	moveValue = -1
	row = -1
	col = -1

	def isGameOn(self,game):
		for i in range(len(game)):
			for j in range(len(game[i])):
				if (game[i][j] == '_'):
					return True
		return False

	def maxvalue(self,game):
		#print "Inside maxvalue"
		v = -1000
		for i in range(len(game)):
			for j in range(len(game[i])):
				if (game[i][j] == '_'):
					game[i][j] = self.player
					v = max(v,self.maxvalue(game))
					game[i][j] = '_'
		return v;

	def minvalue(self,game):
		#print "Inside minvalue"
		v = 1000
		for i in range(len(game)):
			for j in range(len(game[i])):
				if (game[i][j] == '_'):
					game[i][j] = self.opponent
					v = min(v,self.minvalue(game))
					game[i][j] = '_'
		return v;

	def value(self,game):
		if (tictactoe().isGameOn(game) == False):
			print "This is EndGame"
			return self.bestValue
		if (self.turn == 'x'):
			return tictactoe().maxvalue(game)
		else:
			return tictactoe().minvalue(game)

	def utility(self,game):
		for i in range(len(game)):
			for j in range(len(game[i])):
				#print game[i][j] 
				if (game[i][j] == '_'):
					game[i][j] = self.player
					self.moveValue = tictactoe().value(game)
					game[i][j] = '_'
					if (self.moveValue > self.bestValue):
						row = i
						col = j
						self.bestValue = self.moveValue
						#print self.moveValue






print "Start"
game = [['o','o','x'],
		['x','_','o'],
		['_','_','x']]

print game

obj = tictactoe()
obj.utility(game)