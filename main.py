from dao.dao import Dao
from ui.main_ui import MainUI
from controller.main_controller import MainController
from ui.board_ui import BoardUI


def main():
    dao = Dao()
    ui = MainUI()
    board_ui = BoardUI()
    controller = MainController(ui, board_ui, dao)

if __name__ == '__main__':
    main()