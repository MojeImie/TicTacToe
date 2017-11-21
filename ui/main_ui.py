import os, sys

class MainUI:

    menu = ['Show highscore', 'Start game 1 vs 1', 'Start game 1 vs Computer', 'EndGame']
    title = 'Hello!\nZiemo presents:\nTicTacToeGame!!!\n\n'
    title1 = 'Best of the best\n\n'

    @staticmethod
    def print(it):
        print(it)

    @staticmethod
    def pause():
        input('Press enter..')

    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def create_menu(title, menu):
        for n,option in enumerate(menu,1):
            title += "{}.{}\n".format(n, option)
        return title

    @staticmethod
    def user_choice(menu):
        user = 0
        while user > len(menu) or user < 1:
            try:
                user = int(input('choose option: '))
            except ValueError:
                print('invalid value!')
        return user

    @staticmethod
    def new_player_inputs():
        name = input('Type your name:')
        country = input('Type your country: ')
        return name, country
        