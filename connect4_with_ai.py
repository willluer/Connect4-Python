from utils import *
from PlayerExample import PlayerExample
import numpy as np
import random
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER_1 = PlayerExample("p1")
PLAYER_2 = PlayerExample("p2")

EMPTY = 0
PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2

WINDOW_LENGTH = 4


board = create_board(ROW_COUNT,COLUMN_COUNT)
print_board(board)
game_over = False

# pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

# screen = pygame.display.set_mode(size)
# draw_board(board,screen)
# pygame.display.update()

# myfont = pygame.font.SysFont("monospace", 75)

starting_turn = random.choice([PLAYER_1.player_id, PLAYER_2.player_id])

n_games = 500
games_played = 0
scores = {}
scores[PLAYER_1.player_id] = 0
scores[PLAYER_2.player_id] = 0
scores["ties"] = 0

while games_played < n_games:
	board = create_board(ROW_COUNT,COLUMN_COUNT)
	game_over = False
	turn = starting_turn

	while not game_over:
		move = COLUMN_COUNT + 1

		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()
		#
		# 	if event.type == pygame.MOUSEMOTION:
		# 		pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
		# 		posx = event.pos[0]
		# 		if turn == PLAYER_1:
		# 			pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
		#
		# 	pygame.display.update()
		#
		# 	if event.type == pygame.MOUSEBUTTONDOWN:
		# 		pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
		# 		#print(event.pos)
		# 		# Ask for Player 1 Input
		if is_tie_game(board):
			# print_board(board)
			# print("Tie game")
			scores["ties"] += 1
			game_over = True

		if turn == PLAYER_1.player_id and not game_over:
			# while not is_valid_location(board,move):
			move = PLAYER_1.get_next_move(board)
			if is_valid_location(board, move):
				row = get_next_open_row(board, move)
				drop_piece(board, row, move, PLAYER_1_PIECE)

				if winning_move(board, PLAYER_1_PIECE):
					# label = myfont.render("Player 1 wins!!", 1, RED)
					# print_board(board)
					scores[PLAYER_1.player_id] += 1
					# print("{} wins the game".format(PLAYER_1.player_id))
					# screen.blit(label, (40,10))
					game_over = True
			else:
				raise Exception("Are you fucking kidding me {}, make your AI give a valid move".format(PLAYER_1.player_id))


		# Ask for Player 2 Input
		elif turn == PLAYER_2.player_id and not game_over:
			move = PLAYER_2.get_next_move(board)
			if is_valid_location(board, move):
				row = get_next_open_row(board, move)
				drop_piece(board, row, move, PLAYER_2_PIECE)

				if winning_move(board, PLAYER_2_PIECE):
					# label = myfont.render("Player 2 wins!!", 1, YELLOW)
					# screen.blit(label, (40,10))
					# print_board(board)
					scores[PLAYER_2.player_id] += 1
					# print("{} wins the game".format(PLAYER_2.player_id))
					game_over = True
			else:
				raise Exception("Are you fucking kidding me {}, make your AI give a valid move".format(PLAYER_2.player_id))


		turn = PLAYER_1.player_id if turn == PLAYER_2.player_id else PLAYER_2.player_id
		# print_board(board)

	games_played +=1
	starting_turn = PLAYER_1.player_id if starting_turn == PLAYER_2.player_id else PLAYER_2.player_id

print(scores)
