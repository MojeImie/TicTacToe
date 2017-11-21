from model.mark import Mark
from model.player import Player

class Board:

    def __init__(self):
        self.marks = [Mark(i) for i in range(1,10)]
        
    

    