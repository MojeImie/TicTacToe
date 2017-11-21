from model.mark import Mark
from model.board import Board
import random
import datetime

class BoardController:

    def __init__(self, ui, player1, player2=None):
        self.ui = ui
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.start_controller()
    
    def start_controller(self):
        self.draw_random_starter()
        
    def draw_random_starter(self, comp_vs_player=None):
        if comp_vs_player:
            pass
        else:
            self.draw = [self.player1, self.player2]
            random.shuffle(self.draw)
            self.draw[0].sign = 'cross'
            self.draw[1].sign = 'circle'
            self.insert_mark()

    def insert_mark(self):
        self.breakk = False
        self.start = True
        while self.start:
            self.ui.clear()
            self.ui.print(self.ui.create_board(Mark.free))
            player_active = self.draw[0]
            self.check_winner(player_active.sign, self.draw[1])
            if self.breakk:
                return

            self.ui.print('Your turn {}'.format(self.draw[0].name))
            choose = self.ui.choose_place()
            for mark in Mark.free:
                if mark.number == choose:
                    if player_active.sign == 'cross':
                        mark.active_cross()
                    else:
                        mark.active_circle()

            self.draw[0], self.draw[1] = self.draw[1], self.draw[0]

    def check_winner(self, mark, player):
        if mark == 'cross':
            mark = Mark.all_circle
        else:
            mark = Mark.all_cross

        if len(mark) >= 3:
            for i in range(2, len(mark)):
                if mark[i-2].number != 5 and mark[i-2].number != 6 and mark[i].number != 4 and mark[i].number != 5: 
                    if (mark[i].number - mark[i-1].number) - (mark[i-1].number - mark[i-2].number) == 0:
                        self.start = False
                        self.breakk = True
                        return self.end_(player)

    def end_(self, player):
        player.won += 1
        player.last_game = datetime.date.today()
        Mark.delete()
        self.ui.print(self.ui.end_game(player.name))
        self.ui.pause()