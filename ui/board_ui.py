from ui.main_ui import MainUI

class BoardUI(MainUI):

    not_allowed_num = []

    @staticmethod
    def create_board(marks):
        first_row = '╔══╦══╦══╗'              
        last_row =  '║\n╚══╩══╩══╝'
        space = '╠══╬══╬══╣'
        middle = '' 
        for n,mark in enumerate(marks,1):
            if n == 3 or n == 6:
                middle += "║ {}║\n{}\n".format(mark, space)
            else: 
                middle += "║ {}".format(mark)
                
        return "{}\n{}{}\n".format(first_row, middle, last_row)

    def choose_place(self):
        user = 0
        while user > 9 or user < 1 or user in BoardUI.not_allowed_num:
            try:
                user = int(input('Choose number assigns to specify area: '))
            except ValueError:
                print('Only number allowed!')
                self.pause()
        BoardUI.not_allowed_num.append(user)
        return user
    
    @staticmethod
    def end_game(player):
        pic = '''
             ---,_,----
            /    .     \/
           /     |      \/
          (      @@      )
          /   _/----\_   \/
         /   '/      \`   \	
        /    /   .    \    \     
       /    /|        |\    \/
       /   / |        | \   \/
      /   /`_/_      _\_'\   \/
     /  '/  (  . )( .  )  \  `\/
     <_ ' `--`___'`___'--' ` _>
    /  '     @ @/ =\@ @     `  \/
   /  /      @@(  , )@@      \  \/
  /  /       @@| o o|@@       \  \/
 ' /          @@@@@@@@          \ ` Little White Rabbit 

    '''
        out = "Bravo {}, you won this game!\n{}".format(player, pic)
        return out