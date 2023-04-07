import random
import numpy as np
import tensorflow as tf


# abstract class for player
class Player(object):
    # constant for player names
    X = "X"
    O = "O"

    def __init__(self, name):
        self.name = name

    def make_move(self, board, verbose=False):
        pass

    def __str__(self):
        return self.name


# random player
class RandomPlayer(Player):
    def make_move(self, board, verbose=False):
        """
        Makes a move on the board
        :param verbose:
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
    def make_move(self, board, verbose=False):
        """
        Makes a move on the board
        :param verbose:
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

class AIPlayer(Player):
    def __init__(self, name, h5_file):
        """
        Takes a path to an h5 file and loads the model
        :param name:
        :param model:
        """
        super().__init__(name)

        # load model
        self.model = tf.keras.models.load_model(h5_file)

    def make_move(self, board, verbose=False):
        """
        Makes a move on the board
        :param verbose:
        :param board:
        :return:
        """

        # get current board flattened
        current_board = [item for sublist in board.board for item in sublist]

        # convert strings of names into 1s for this player and 2s for the other player
        current_board = [1 if x == self.name else 2 if x != 0 else 0 for x in current_board]

        # convert to numpy array
        current_board = np.array(current_board)

        # run model
        prediction = self.model.predict(current_board.reshape(1, 9), verbose=False)

        # print the prediction with accuracy of 2 decimal places
        if verbose:
            print("Prediction: %s" % np.around(prediction, 3))

        is_valid = False
        move = None
        moves = board.get_available_moves()

        if len(moves) == 0:
            return

        # while the move is not valid
        while not is_valid:
            # get the move with the highest probability
            move = np.argmax(prediction)

            # convert to row and column
            move = (move // 3, move % 3)

            # check if the move is valid
            if move in moves:
                is_valid = True
            else:
                # if not valid, set the probability of that move to 0 and try again
                prediction[0][move[0] * 3 + move[1]] = 0

        board.make_move(move, self)