# Description: Tic Tac Toe Game
class Game(object):
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_player = player1

    def play(self, verbose=False):
        """
        Plays the game
        :return:
        """
        while not self.board.is_game_over():
            if verbose:
                self.board.display()
            self.current_player.make_move(self.board, verbose=verbose)
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        if verbose:
            self.board.display()
            if self.board.is_draw():
                print("It's a draw!")
            else:
                print("Player %s wins!" % self.board.winner)

    def to_training_data(self, perspective_from_first_move=True):
        """
        Converts the played game to a training data array. The array contains dicts which store the board state and the
        next move and the probability to win the game for that move.
        It assumes the AI is player 1 and the opponent is player 2.

        The array contains dicts with the following keys:
        - board: the board state as an array with 9 elements
        - move: the move that was made wheighted by the duration of the game
        :return:
        """

        # create the training data array
        training_data = []

        # create the board array
        board = [0 for _ in range(9)]

        # get the duration of the game
        duration = len(self.board.move_history)

        # if the game was lost by the AI cut duration by 2
        opponent_won = \
            self.board.winner == self.player2.name if perspective_from_first_move else \
                self.board.winner == self.player1.name

        if opponent_won:
            duration -= 2

        # iterate over the moves
        for i in range(duration):
            # get the move
            move = self.board.move_history[i]

            # if the move was made by the AI
            if i % 2 == 0:
                # calculate the move score
                move_score = 1 if not opponent_won else 0

                # wheight the move by the duration of the game
                if not opponent_won:
                    if duration == 5:
                        move_score = 4
                    elif duration == 6:
                        move_score = 3
                    elif duration == 7:
                        move_score = 2
                    elif duration == 8:
                        move_score = 1.5

                # REMOVE THIS!
                if not perspective_from_first_move:
                    move_score *= -1

                # encode the move
                encoded_move = [0 for i in range(9)]
                encoded_move[move[0] * 3 + move[1]] = move_score

                # create the training data dict
                training_data_dict = {
                    "board": board.copy(),
                    "move": encoded_move
                }

                # append the training data dict to the array
                training_data.append(training_data_dict)

            # update the board
            is_ai_move = \
                i % 2 == 0 if perspective_from_first_move else \
                i % 2 == 1
            board[move[0] * 3 + move[1]] = 1 if is_ai_move else 2

        # if the game was lost by the AI replace the last move with the opponent's move and wheight it by 5
        if opponent_won:
            # get the move
            move = self.board.move_history[-1]

            # encode the move
            encoded_move = [.1 if i != 0 else 0 for i in range(9)]
            encoded_move[move[0] * 3 + move[1]] = .75

            # create the training data dict
            training_data_dict = {
                "board": board.copy(),
                "move": encoded_move
            }

            # append the training data dict to the array
            training_data.append(training_data_dict)

        # return the training data array
        return training_data
