# import random
import random


# abstract class for player
class Player(object):
    # constant for player names
    X = "X"
    O = "O"

    def __init__(self, name):
        self.name = name

    def make_move(self, board):
        pass

    def __str__(self):
        return self.name


# random player
class RandomPlayer(Player):
    def make_move(self, board):
        """
        Makes a move on the board
        :param board:
        :return:
        """
        moves = board.get_available_moves()
        if len(moves) == 0:
            return
        move = random.choice(moves)
        board.make_move(move, self)


# Human player
class HumanPlayer(Player):
    def make_move(self, board):
        """
        Makes a move on the board
        :param board:
        :return:
        """
        moves = board.get_available_moves()
        if len(moves) == 0:
            return
        print("Available moves: %s" % moves)
        move = input("Enter your move: ")
        move = move.split(",")
        move = (int(move[0]), int(move[1]))

        while move not in moves:
            print("Invalid move!")
            move = input("Enter your move: ")
            move = move.split(",")
            move = (int(move[0]), int(move[1]))

        board.make_move(move, self)