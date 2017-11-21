import csv, os, sys
import datetime
from model.player import Player

class Dao:

    @staticmethod
    def load_scores():
        if not os.path.isfile('static/scores.csv'):
            raise FileNotFoundError
        else:
            with open('static/scores.csv', 'r', encoding='utf16') as file:
                for row in file:
                    row = row.strip('\n')
                    row = row.split(',')
                    name = row[0]
                    country = row[1]
                    won = int(row[2])
                    year, month, day = row[3].split('-')
                    date = datetime.date(int(year), int(month), int(day))
                    Player(name, country, won, date)

    @staticmethod
    def save_scores():
        with open('static/scores.csv', 'w', encoding='utf16') as file:
            writer = csv.writer(file)
            for player in Player.all_players:
                if player.last_game:
                    writer.writerow([player.name, player.country, player.won, player.last_game])