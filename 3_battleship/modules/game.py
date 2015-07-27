import uuid


class Game(object):
    """docstring for Battleship_Game"""
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
