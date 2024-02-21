import random
import time
import pygame
import math
from connect4 import connect4

class connect4Player(object):
	def __init__(self, position, seed=0, CVDMode=False):
		self.position = position
		self.opponent = 1 if position == 2 else 2
		self.seed = seed
		random.seed(seed)
		if CVDMode:
			global P1COLOR
			global P2COLOR
			P1COLOR = (227, 60, 239)
			P2COLOR = (0, 255, 0)

	def play(self, env: connect4, move: list) -> None:
		move = [-1]

class human(connect4Player):

	def play(self, env: connect4, move: list) -> None:
		move[:] = [int(input('Select next move: '))]
		while True:
			if int(move[0]) >= 0 and int(move[0]) <= 6 and env.topPosition[int(move[0])] >= 0:
				break
			move[:] = [int(input('Index invalid. Select next move: '))]

class human2(connect4Player):

	def play(self, env: connect4, move: list) -> None:
		done = False
		while(not done):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEMOTION:
					pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
					posx = event.pos[0]
					if self.position == 1:
						pygame.draw.circle(screen, P1COLOR, (posx, int(SQUARESIZE/2)), RADIUS)
					else: 
						pygame.draw.circle(screen, P2COLOR, (posx, int(SQUARESIZE/2)), RADIUS)
				pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))
					move[:] = [col]
					done = True

class randomAI(connect4Player):

	def play(self, env: connect4, move: list) -> None:
		possible = env.topPosition >= 0
		indices = []
		for i, p in enumerate(possible):
			if p: indices.append(i)
		move[:] = [random.choice(indices)]

class stupidAI(connect4Player):

	def play(self, env: connect4, move: list) -> None:
		possible = env.topPosition >= 0
		indices = []
		for i, p in enumerate(possible):
			if p: indices.append(i)
		if 3 in indices:
			move[:] = [3]
		elif 2 in indices:
			move[:] = [2]
		elif 1 in indices:
			move[:] = [1]
		elif 5 in indices:
			move[:] = [5]
		elif 6 in indices:
			move[:] = [6]
		else:
			move[:] = [0]

class minimaxAI(connect4Player):

    def play(self, env: connect4, move: list) -> None:
 
        # Maximum Search Depth
        DEPTH = 2
        
#        # Hard Code the First Move
#        if not len(env.history[self.position - 1]):
#            if len(env.history[self.opponent.position - 1]) and env.history[self.opponent.position - 1][0] == 3: move[:] = [2]
#            else: move[:] = [3]
#            return
        
        # Simulate to Find Nash Equillibrium Move
        start = time.time()
        value, best_move = self.maxValue(env, DEPTH)
        end = time.time()
        move[:] = [best_move]
        
        # Print if Minimax Executed Completely
        print(f"MinimaxAI Executed Successfully in {end - start}. Nash Equillibrium: {value}, Move: {best_move}")
        
        
    def maxValue(self, env, depth):
        
        player = self.position
        
        # Get the List of Possible Moves
        possible = env.topPosition >= 0
        indices = []
        for i, p in enumerate(possible):
            if p: indices.append(i)
        
        # Terminal State Test
        if depth == 0: return self.eval_board(env), None
        if len(indices) == 0: return self.eval_board(env), None
        
        # Initialize Value to Negative Infinity
        max_value = -math.inf
        
        # Check every successor game state
        move = None
        for i in indices:
            
            # Simulate the successor state
            new_env = env.getEnv()
            self.simulateMove(new_env, i, player)
            
            # Check if Game is Over
            if new_env.gameOver(i, player): return 1000, i
            
            # Check Value of the Sucessor State
            value, _ = self.minValue(new_env, (depth - 1))
            if value > max_value:
                max_value = value
                move = i
                
        return max_value, move
        
        
    def minValue(self, env, depth):
        
        switch = {1:2, 2:1}
        player = switch[self.position]
        
        # Get the List of Possible Moves
        possible = env.topPosition >= 0
        indices = []
        for i, p in enumerate(possible):
            if p: indices.append(i)
            
        # Terminal State Test
        if depth == 0: return self.eval_board(env), None
        if len(indices) == 0: return self.eval_board(env), None
        
        # Initialize Value to Negative Infinity
        min_value = math.inf
        
        # Check every successor game state
        move = None
        for i in indices:
            
            # Simulate the successor state
            new_env = env.getEnv()
            self.simulateMove(new_env, i, player)
            
            # Check if Game is Over
            if new_env.gameOver(i, player): return -1000, i
            
            # Check Value of the Sucessor State
            value, _ = self.maxValue(new_env, (depth - 1))
            if value < min_value:
                min_value = value
                move = i
                
        return min_value, move
        
    
    def simulateMove(self, env, move, player):
        env.board[env.topPosition[move]][move] = player
        env.topPosition[move] -= 1
        env.history[0].append(move)
        
        
    def eval_board(self, env):
        
        # Get the Game Board
        board = env.getBoard()
        
        # Initialize Player Arrays to Store Consecutive Pieces
        p1_eval, p2_eval = [0 for _ in range(4)], [0 for _ in range(4)]
        p1_count, p2_count = [0], [0]
        
        # Horizontal Evaluation
        for i in range(env.shape[0]):
            for j in range(env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
                    
        # Vertical Evaluation
        for j in range(env.shape[1]):
            for i in range(env.shape[0]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
        
        # Diagonal Evaluations (Bottom Left to Top Right)
        col = 0
        for row in range(env.shape[0]):
            i, j = row, col
            while (i > -1) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i -= 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
        row = env.shape[0] - 1
        for col in range(1, env.shape[1]):
            i, j = row, col
            while (i > -1) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i -= 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
            
        # Diagonal Evaluations (Top Left to Bottom Right)
        col = 0
        for row in range(env.shape[0]):
            i, j = row, col
            while (i < env.shape[0]) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i += 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
        row = 0
        for col in range(1, env.shape[1]):
            i, j = row, col
            while (i < env.shape[0]) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i += 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
            
        # Get the utility of each player
        weights = [1, 10, 100, 1000]
        dot = lambda a, b: sum(x * y for x, y in zip(a, b))
        p1_util = dot(p1_eval, weights)
        p2_util = dot(p2_eval, weights)
        
        # Return the final evaluation
        if self.position == 1: return p1_util - p2_util
        else: return p2_util - p1_util
    
            
    def eval_piece(self, value, p1_count, p2_count, p1_eval, p2_eval):
        if value == 1:
            p1_count[0] += 1
            if p2_count[0]: p2_eval[min(3, (p2_count[0] - 1))] += 1
            p2_count[0] = 0
        elif value == 2:
            p2_count[0] += 1
            if p1_count[0]: p1_eval[min(3, (p1_count[0] - 1))] += 1
            p1_count[0] = 0
        else:
            if p1_count[0]: p1_eval[min(3, (p1_count[0] - 1))] += 1
            if p2_count[0]: p2_eval[min(3, (p2_count[0] - 1))] += 1
            p1_count[0] = 0
            p2_count[0] = 0
            
            
    def eval_overflow(self, p1_count, p2_count, p1_eval, p2_eval):
            if p1_count[0]: p1_eval[min(3, (p1_count[0] - 1))] += 1
            if p2_count[0]: p2_eval[min(3, (p2_count[0] - 1))] += 1
            p1_count[0] = 0
            p2_count[0] = 0
    

class alphaBetaAI(connect4Player):

    def play(self, env: connect4, move: list) -> None:
 
        # Maximum Search Depth
        DEPTH = 3
        
#        # Hard Code the First Move
#        if not len(env.history[self.position - 1]):
#            if len(env.history[self.opponent.position - 1]) and env.history[self.opponent.position - 1][0] == 3: move[:] = [2]
#            else: move[:] = [3]
#            return
        
        # Simulate to Find Nash Equillibrium Move
        start = time.time()
        alpha, beta = -math.inf, math.inf
        value, best_move = self.maxValue(env, DEPTH, alpha, beta)
        end = time.time()
        move[:] = [best_move]
        
        # Print if Minimax Executed Completely
        print(f"AlphaBetaAI Executed Successfully in {end - start}. Nash Equillibrium: {value}, Move: {best_move}")
        
        
    def maxValue(self, env, depth, alpha, beta):
        
        player = self.position
        
        # Get the List of Possible Moves
        possible = env.topPosition >= 0
        indices = []
        for i, p in enumerate(possible):
            if p: indices.append(i)
        
        # Terminal State Test
        if depth == 0: return self.eval_board(env), None
        if len(indices) == 0: return self.eval_board(env), None
        
        # Initialize Value to Negative Infinity
        max_value = -math.inf
        
        # Check every successor game state
        move = None
        for i in indices:
            
            # Simulate the successor state
            new_env = env.getEnv()
            self.simulateMove(new_env, i, player)
            
            # Check if Game is Over
            if new_env.gameOver(i, player): return self.eval_board(new_env), i
            
            # Check Value of the Sucessor State
            value, _ = self.minValue(new_env, (depth - 1), alpha, beta)
            if value > max_value:
                max_value = value
                move = i
                
            # Alpha-Beta Pruning
            if value >= beta: return value, i
            alpha = max(alpha, value)
                
        return max_value, move
        
        
    def minValue(self, env, depth, alpha, beta):
        
        switch = {1:2, 2:1}
        player = switch[self.position]
        
        # Get the List of Possible Moves
        possible = env.topPosition >= 0
        indices = []
        for i, p in enumerate(possible):
            if p: indices.append(i)
            
        # Terminal State Test
        if depth == 0: return self.eval_board(env), None
        if len(indices) == 0: return self.eval_board(env), None
        
        # Initialize Value to Negative Infinity
        min_value = math.inf
        
        # Check every successor game state
        move = None
        for i in indices:
            
            # Simulate the successor state
            new_env = env.getEnv()
            self.simulateMove(new_env, i, player)
            
            # Check if Game is Over
            if new_env.gameOver(i, player): return self.eval_board(new_env), i
            
            # Check Value of the Sucessor State
            value, _ = self.maxValue(new_env, (depth - 1), alpha, beta)
            if value < min_value:
                min_value = value
                move = i
                
            # Alpha-Beta Pruning
            if value <= alpha: return value, i
            beta = min(beta, value)
                
        return min_value, move
        
    
    def simulateMove(self, env, move, player):
        env.board[env.topPosition[move]][move] = player
        env.topPosition[move] -= 1
        env.history[0].append(move)
        
        
    def eval_board(self, env):
        
        # Get the Game Board
        board = env.getBoard()
        
        # Initialize Player Arrays to Store Consecutive Pieces
        p1_eval, p2_eval = [0 for _ in range(4)], [0 for _ in range(4)]
        p1_count, p2_count = [0], [0]
        
        # Horizontal Evaluation
        for i in range(env.shape[0]):
            for j in range(env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
                    
        # Vertical Evaluation
        for j in range(env.shape[1]):
            for i in range(env.shape[0]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
        
        # Diagonal Evaluations (Bottom Left to Top Right)
        col = 0
        for row in range(env.shape[0]):
            i, j = row, col
            while (i > -1) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i -= 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
        row = env.shape[0] - 1
        for col in range(1, env.shape[1]):
            i, j = row, col
            while (i > -1) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i -= 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
            
        # Diagonal Evaluations (Top Left to Bottom Right)
        col = 0
        for row in range(env.shape[0]):
            i, j = row, col
            while (i < env.shape[0]) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i += 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
        row = 0
        for col in range(1, env.shape[1]):
            i, j = row, col
            while (i < env.shape[0]) and (j < env.shape[1]):
                self.eval_piece(board[i,j], p1_count, p2_count, p1_eval, p2_eval)
                i += 1
                j += 1
            self.eval_overflow(p1_count, p2_count, p1_eval, p2_eval)
            
        # Get the utility of each player
        weights = [1, 10, 100, 1000]
        dot = lambda a, b: sum(x * y for x, y in zip(a, b))
        p1_util = dot(p1_eval, weights)
        p2_util = dot(p2_eval, weights)
        
        # Return the final evaluation
        if self.position == 1: return p1_util - p2_util
        else: return p2_util - p1_util
    
            
    def eval_piece(self, value, p1_count, p2_count, p1_eval, p2_eval):
        if value == 1:
            p1_count[0] += 1
            if p2_count[0]: p2_eval[min(3, (p2_count[0] - 1))] += 1
            p2_count[0] = 0
        elif value == 2:
            p2_count[0] += 1
            if p1_count[0]: p1_eval[min(3, (p1_count[0] - 1))] += 1
            p1_count[0] = 0
        else:
            if p1_count[0]: p1_eval[min(3, (p1_count[0] - 1))] += 1
            if p2_count[0]: p2_eval[min(3, (p2_count[0] - 1))] += 1
            p1_count[0] = 0
            p2_count[0] = 0
            
            
    def eval_overflow(self, p1_count, p2_count, p1_eval, p2_eval):
            if p1_count[0]: p1_eval[min(3, (p1_count[0] - 1))] += 1
            if p2_count[0]: p2_eval[min(3, (p2_count[0] - 1))] += 1
            p1_count[0] = 0
            p2_count[0] = 0

        
        
SQUARESIZE = 100
BLUE = (0,0,255)
BLACK = (0,0,0)
P1COLOR = (255,0,0)
P2COLOR = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)




