class Board(object):
    def __init__(self):
        self.size = 3
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.winner = 0
        self.move_history = []

    def get_available_moves(self):
        """
        Returns a list of available moves
        :return:
        """
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    moves.append((i, j))
        return moves

    def make_move(self, move, player):
        """
        Makes a move on the board
        :param move:
        :param player:
        :return:
        """
        self.board[move[0]][move[1]] = player.name
        self.move_history.append(move)

    def is_game_over(self):
        """
        Checks if the game is over
        :return:
        """
        # check rows
        for i in range(self.size):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.winner = self.board[i][0]
                return True

        # check columns
        for i in range(self.size):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.winner = self.board[0][i]
                return True

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][2]
            return True

        # check if draw
        if len(self.get_available_moves()) == 0:
            return True

        return False

    def is_draw(self):
        """
        Checks if the game is a draw
        :return:
        """
        return self.is_game_over() and self.winner == 0

    def display(self):
        """
        Displays the board
        :return:
        """
        print(self)

    def __str__(self):
        s = "-----\n"
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    s += " "
                else:
                    s += self.board[i][j]
                if j < self.size - 1:
                    s += "|"
            if i < self.size - 1:
                s += "\n"
        s += "\n-----"
        return s