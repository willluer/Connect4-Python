from utils import *
from Player import Player
import random

class PlayerExample(Player):
    def __init__(self,player_id):
        super().__init__(player_id)

    def get_next_move(self,state):
        valid_moves = get_valid_locations(state)
        return random.choice(valid_moves)
