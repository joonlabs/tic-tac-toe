# create a new game with two players and a board
from tictactoe.player import HumanPlayer, AIPlayer, Player
from tictactoe.board import Board
from tictactoe.game import Game

ai_player = AIPlayer(Player.X, "models/model.h5")
human_player = HumanPlayer(Player.O)
while True:
    game = Game(human_player, ai_player, Board())
    #game = Game(ai_player, human_player, Board())

    # play the game
    game.play(verbose=True)