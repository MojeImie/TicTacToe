from model.mark import Mark
from model.board import Board
from model.player import Player
import random
import datetime

class BoardController:

    def __init__(self, ui, player1, player2=None):
        self.ui = ui
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        if not self.player2:
            self.AI = [player for player in Player.all_players if player.name == 'Computer'][0]
        self.start_controller()


    def start_controller(self):
        if self.player2:
            self.draw_random_starter()
        else:
            self.draw_random_starter('comp')
            
    def draw_random_starter(self, comp_vs_player=None):
        if comp_vs_player:
            self.draw = [self.player1, self.AI]
            random.shuffle(self.draw)
            self.draw[0].sign = 'cross'
            self.draw[1].sign = 'circle'
            self.insert_mark_AI()
        else:
            self.draw = [self.player1, self.player2]
            random.shuffle(self.draw)
            self.draw[0].sign = 'cross'
            self.draw[1].sign = 'circle'
            self.insert_mark()
#########################AI
    def insert_mark_AI(self):
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
            if self.draw[0].name != 'Computer' and self.draw[0].country != 'World':
                choose = self.ui.choose_place()
            else:
                choose = self.AI_handle(player_active.sign)

            for mark in Mark.free:
                if mark.number == choose:
                    if player_active.sign == 'cross':
                        mark.active_cross()
                    else:
                        mark.active_circle()

            self.draw[0], self.draw[1] = self.draw[1], self.draw[0]
    
    def AI_handle(self, mark):

        if mark == 'cross':
            AI_marks = Mark.all_circle
            Player_marks = Mark.all_cross
        else:
            Player_marks = Mark.all_circle
            AI_marks = Mark.all_cross

        

        if len(AI_marks) > 1:
            for i in range(1, len(AI_marks)):
                for mark in Mark.free:
                    if mark.number == prediction and prediction not in self.ui.not_allowed():
                        diff = AI_marks[i].number - AI_marks[i-1].number
                        prediction = AI_marks[i].number + diff 
                        if all(number != prediction for number in [1,2,4,5]):
                            self.ui.add(prediction)
                            return prediction


                        prediction = AI_marks[i-1].number - diff
                # for mark in Mark.free:
                    # elif mark.number == prediction and prediction not in self.ui.not_allowed():
                        elif all(number != prediction for number in [5,6,8,9]):
                            self.ui.add(prediction)
                            return prediction
                

                        diff = (AI_marks[i].number - AI_marks[i-1].number)/2
                        prediction = AI_marks[i].number - diff
                # for mark in Mark.free:
                    # elif mark.number == prediction and prediction not in self.ui.not_allowed():
                        elif all(number != prediction for number in [1,3,7,9]):
                            self.ui.add(prediction)
                            return prediction
                        # else:
                            # return random.choice([mark.number for mark in Mark.free if not mark.circle and not mark.cross])
                        
        else:
            return random.choice([mark.number for mark in Mark.free if not mark.circle and not mark.cross])
                



#########################

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
        self.ui.delete()
        Mark.delete()
        self.ui.print(self.ui.end_game(player.name))
        self.ui.pause()

    