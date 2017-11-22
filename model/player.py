class Player:

    all_players = []

    def __init__(self, name, country, won=0, last_game=None):
        self.name = name
        self.country = country
        self.won = won
        self.last_game = last_game 
        self.sign = None
        Player.all_players.append(self)

    def upgrade_score(self):
        self.won += 1

    def __str__(self):
        out = '{} {} {} {}'.format(self.name, self.country, self.won, self.last_game)
        return 

    def asdasd(asf):
        pass

    def kolejny():
        pass