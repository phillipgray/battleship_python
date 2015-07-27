import uuid
from player import Player


class Game(object):
    """docstring for Battleship_Game"""
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
        self.turn_counter = 0
        self.is_online = False
        self.player_1 = Player()
        self.player_2 = None

    def incr_turn_counter(self):
        self.turn_counter += 1
