import math


class Tic_Tac_Toe():
    def __init__(self, board_size: int):
        # 1 = x, 0 = 0
        self.board_size = board_size
        # self.board = [" " * board_size for i in range(board_size)]
        self.board = [[0 for i in range(self.board_size)] for j in range(self.board_size)]
        self.decode = {0: " ", 1: "X", -1: "0"}

    def print_game_board(self):
        print(" ___" * self.board_size)
        template = "| {} " * self.board_size + "|"
        for item in self.board:
            print(template.format(*[self.decode[i] for i in item]))
            print(" ___" * self.board_size)

    def check_win(self):
        # check row
        for rows in self.board:
            if math.fabs(sum(rows)) == self.board_size:
                return True
        # check columns
        for columns in zip(*self.board):
            if math.fabs(sum(columns)) == self.board_size:
                return True
        # check diag
        main_diag = sum([self.board[i][i] for i in range(len(self.board))])
        reversal_diag = sum([self.board[-i - 1][i] for i in range(len(self.board))])
        if math.fabs(main_diag) == self.board_size or math.fabs(reversal_diag) == self.board_size:
            return True
        return False

    def write_user_note(self, pos: list, write_type):
        i, j = pos
        self.board[i][j] = write_type

    def user_game(self):
        while True:
            # user 1 step
            u1 = list(map(int, input("U1:\n").split()))
            self.write_user_note(u1, 1)
            self.print_game_board()
            if self.check_win():
                return "User 1 win"

            u2 = list(map(int, input("U2:\n").split()))
            self.write_user_note(u2, -1)
            self.print_game_board()
            if self.check_win():
                return "User 2 win"


def test_check_win(array: list, real_ans):
    cls = Tic_Tac_Toe(len(array))
    cls.board = array
    print("{} - {}".format(cls.check_win(), real_ans))


# check correct funk
template = [[-1, 1, 0], [1, -1, 1], [0, -1, 0]]
template1 = [[-1, 0, 1], [-1, 0, 0], [-1, 1, 1]]
template2 = [[-1, 0, 1], [0, -1, 1], [1, 0, -1]]
test_check_win(template, False)
test_check_win(template1, True)
test_check_win(template2, True)

cls = Tic_Tac_Toe(3)
cls.user_game()
