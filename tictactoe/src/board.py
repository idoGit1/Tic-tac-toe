
from const import *

class Board:
    def __init__(self):
        self.squares = [[-10, -10, -10] for col in range(COLS)]
        self.last_move = None
        
