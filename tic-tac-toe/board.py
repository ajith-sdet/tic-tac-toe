class Board:
	
	def __init__(self,r,c,player1, player2):
		self.r = int(r)
		self.c = int(c)
		self.board = [[0 for _ in range(self.c)] for _ in range(self.r)]
		self.player1 = player1
		self.player2 = player2
		self.move_symbol = {self.player1:1, self.player2:-1}

	
	def choose_start(self):
		choose_player = input("Choose who wants to play the game \n"
							  "1. Player 1. \n"
							  "2. Player 2 \n"
							  "Ans:  ")
		print(choose_player)
		if choose_player == "1":
			self.player1.flag = True
			return True
		if choose_player == "2":
			self.player2.flag = True
			return True
		else:
			print("Please type input as either 1 or 2")
			return False

	def get_player(self):
		if self.player1.flag:
			if self.move(self.player1):
				return True
		else:
			if self.move(self.player2):
				return True
			
	
	def set_flag(self,player1,player2):
		
		if player1.flag == True:
			player1.flag = False
			player2.flag = True
		else:
			player2.flag = False
			player1.flag = True
			

	def check_all_rows_are_same(self,player,row):
		winrow = True
		for i in range(self.r):
			if self.board[row][i] != self.move_symbol[player]:
				winrow = False
		return winrow
	
	def check_all_columns_are_same(self,player,row):
		winrow = True
		for i in range(self.r):
			if self.board[i][row] != self.move_symbol[player]:
				winrow = False
		return winrow
	
	
	
	def get_winner(self,player,row):
		v_row = self.check_all_rows_are_same(player,row)
		v_column = self.check_all_columns_are_same(player,row)
		
		if v_row or v_column:
			return True
	
	def drawn(self):
		
		for i in range(self.r):
			for j in range(self.c):
				if self.board[i][j] == 0:
					return False
		return True
		
	
	def move(self,player):
		print(f"{player.name} needs to move in the game")
		print("Which row and column , do you want to put your symbol")
		r = int(input("Enter the row value: "))
		c = int(input("Enter the column value: "))
		
		if player == self.player1:
			if self.board[r][c] == 0:
				self.board[r][c] = self.move_symbol[self.player1]
		else:
			if self.board[r][c] == 0:
				self.board[r][c] = self.move_symbol[self.player2]
				
		if self.get_winner(player,r):
			print(f"{player.name} has won the game")
			return True
		
		if self.drawn():
			print("The game is drawn")
			return True
			
		if player == self.player1:
			self.set_flag(self.player1,self.player2)
		else:
			self.set_flag(self.player2, self.player1)
		


class Player:
	
	def __init__(self,name, flag = None):
		self.name = name
		self.flag = None
	

p1 = Player("aji")

p2 = Player("bab")

g1 = Board(3,3,p1,p2)


def play():
	while g1.choose_start():
		# pp.pprint(g1.board)
		while not g1.get_player():
			for row in g1.board:
				print(*row , sep = " ")
		break
	else:
		play()
play()
