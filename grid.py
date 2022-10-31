from settings import LEVEL_X_DIM
from settings import *


class Grid():
    def __init__(self):
        self.grid = [[0]*LEVEL_ROWS for i in range(LEVEL_COLS)]
