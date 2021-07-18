class Board:

    def display(self, matrix, score, marker):
        print("\n")
        print(f"Current Stats for Player:\n{marker} - {score}\n")
        print("Column\n  0 1 2")
        print("0", matrix[(0, 0)] + "|" + matrix[(0, 1)] + "|" + matrix[(0, 2)])
        print("  -+-+-")
        print("1", matrix[(1, 0)] + "|" + matrix[(1, 1)] + "|" + matrix[(1, 2)])
        print("  -+-+-")
        print("2", matrix[(2, 0)] + "|" + matrix[(2, 1)] + "|" + matrix[(2, 2)])
        print("  -+-+-")
        print("\n")


class Matrix:
    matrix = {(0, 0): " ", (0, 1): " ", (0, 2): " ", (1, 0): " ",
              (1, 1): " ", (1, 2): " ", (2, 0): " ", (2, 1): " ",
              (2, 2): " "}

    def __init__(self):
        self.matrix_height = 3
        self.matrix_width = 3

    def print_to_board(self, score, marker):
        board = Board()
        board.display(self.matrix, score, marker)

    def amend_matrix(self, row, column, marker):

        if row >= self.matrix_height or column >= self.matrix_width:
            raise IndexError(
                "This is a TIC-TAT-TOE game and has 3 rows and 3 columns")
        elif self.matrix[(row, column)] != " ":
            print("Please enter a valid move - index already in use")
            return

        else:
            self.matrix[(row, column)] = marker

    def check_win_status(self, row, column, score):

        # inspired/ copied from https://codereview.stackexchange.com/questions/24764/tic-tac-toe-victory-check

        if self.matrix[(0, column)] == self.matrix[(1, column)] == self.matrix[(2, column)]:
            return True
        if self.matrix[(row, 0)] == self.matrix[(row, 1)] == self.matrix[(row, 2)]:
            return True
        if row == column and self.matrix[(0, 0)] == self.matrix[(1, 1,)] == self.matrix[(2, 2)]:
            return True
        if row + column == 2 and self.matrix[(0, 2)] == self.matrix[(1, 1)] == self.matrix[(2, 0)]:
            return True

    def refresh_matrix(self):

        for keys, _ in self.matrix.items():
            self.matrix[keys] = " "


class User:
    move = Matrix()

    def __init__(self, score=0):
        self.marker = "o"
        self.score = score

    def make_move(self, row, column):
        self.move.amend_matrix(row, column, self.marker)
        self.move.print_to_board(self.score, self.marker)
        if self.move.check_win_status(row, column, self.score):
            self.move.refresh_matrix()
            return self.__adjust_score()

    def __adjust_score(self):
        self.score += 1


class Computer(User):

    def __init__(self, score=0):
        super().__init__(score)
        self.marker = "x"
        self.score = score


test_user = User()
test_computer = Computer()

test_user.make_move(0, 0)
test_computer.make_move(1, 1)
