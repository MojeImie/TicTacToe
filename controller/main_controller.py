import sys, os
from controller.board_controller import BoardController
from model.player import Player

class MainController:

    def __init__(self, ui, board_ui, dao):
        self.ui = ui
        self.board_ui = board_ui
        self.dao = dao
        self.dao.load_scores()
        self.ui.clear()
        self.start_controller()

    def start_controller(self):
        while 1:
            self.ui.clear()
            self.ui.print(self.ui.create_menu(self.ui.title, self.ui.menu))
            self.user = self.ui.user_choice(self.ui.menu)
            self.handle_menu()
    
    def handle_menu(self):
        if self.user == 1:
            self.show_highscore()
        elif self.user == 2:
            self.create_player()
            self.create_player('second')
            BoardController(self.board_ui, self.player1, self.player2)
            self.dao.save_scores()   
        elif self.user == 3:
            self.create_player()
            BoardController(self.board_ui, self.player1)
            self.dao.save_scores()    
        elif self.user == 4:
            sys.exit('byebye')
            
    def show_highscore(self):
        self.ui.clear()
        players = sorted(Player.all_players, key=lambda player: player.won, reverse=True)
        self.ui.print(self.ui.create_menu(self.ui.title1, players))
        self.ui.pause()

    def create_player(self, player_second=None):
        name, country = self.ui.new_player_inputs()

        if all(player.name != name for player in Player.all_players):
            if not player_second:
                self.player1 = Player(name, country) 
                return self.player1
            else:
                self.player2 = Player(name, country)
                return self.player2
        else:
            for player in Player.all_players:
                if player.name == name and player.country == country:
                    if not player_second:
                        self.player1 = player
                        return self.player1
                    else:
                        self.player2 = player
                        return self.player2